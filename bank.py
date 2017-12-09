from flask_restful import reqparse, abort, fields, marshal_with, Api, Resource, request
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash, _app_ctx_stack
from models import db, Savings, Checking, Loan, Certificate, Profile
from datetime import datetime
import os

app = Flask(__name__)
api = Api(app)

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.root_path, 'bank_api.db')
))

db.init_app(app)

@app.cli.command('initdb')
def initdb_command():
	db.drop_all()
	db.create_all()

	# create 3 user profiles
	address = Address('374 Main Street', 'Dillsburg', 'PA', '17019')
	user_one = Profile("cate38", "Cate Watkins", address, "cate38@example.com", mobile_phone='6578347234')
	user_two = Profile("leah223", "Leah Bradly", Address('810 Main Street', 'York', 'PA', '17118'), 'leah223@example.com', home_phone='3829428391')
	user_three = Profile("marcia12", "Marcia Fredrickson", Address('773 Temple Rd', 'New Haven', 'CT', '01132'), 'marcia12@example.com', mobile_phone='8392814932')
	db.session.add(user_one)
	db.session.add(user_two)
	db.session.add(user_three)

	# create savings, checking, certificate, and loan for each user
	savings_one = Savings("cate38", "savings accound for cate38", 1000.42, datetime.now())
	savings_two = Savings("leah223", "savings accound for leah223", 583792.83, datetime.now())
	savings_three = Savings("marcia12", "savings accound for marcia12", 100000, datetime.now())
	db.session.add(savings_one)
	db.session.add(savings_two)
	db.session.add(savings_three)

	db.session.commit()

# "/savings/<username>"
class SavingsEndpoint(Resource):
	def get(self, username):
		# given username, get savings data for that user, return data as json
		saving_account = Savings.query.filter_by(username=username).first()
		if saving_account:
			# turn the data from saving_account into json object
			return saving_account.to_dict()
		else:
			return error(400, "Savings doesn't exists under {}".format(username))


# "/checking/<username>"
class CheckingEndpoint(Resource):
	def get(self, username):
		# given username, get checking data for that user, return data as json
		checking_account = Checking.query.filter_by(username=username).first()
		if checking_account:
			# return object
		else:
			return error(400, "Checking doesn't exists under {}".format(username))

# "/loan/<username>"
class LoanEndpoint(Resource):
	def get(self, username):
		# given username, get loan data for that user, return data as json
		loan_account = Checking.query.filter_by(username=username).first()
		if loan_account:
			# return loan_account.to_json()
		else:
			return error(400, "Loan doesn't exists under {}".format(username))

# "/certificate/<username>"
class CertificateEndpoint(Resource):
	def get(self, username):
		# given username, get certificate data for that user, return data as json
		certificate_account = Certificate.query.filter_by(username=username).first()
		if certificate_account:
			# return certificate_account.to_json()
		else:
			return error(400, "Certificate doesn't exists under {}".format(username))

# "/<username>"
class ProfileEndpoint(Resource):
	def get(self, username):
		# given username, get profile for that user, return data as json

	# "/<username>?param=<param>&value=<value>"
	def put(self, username):
		input_data = request.args.to_dict()
		param = input_data['param']
		value = input_data['value']
		input_is_valid, value = valid_input(param, value)
		if input_is_valid:
			user = Profile.query.filter_by(username=username).first()
			if user:
				# update value of param
				update_profile(param, value, user)
				# return profile data for that user, 200
			else:
				return error(400, "{} doesn't exist".format(username))
		else:
			return error(400, "Param {} or value {} is invalid".format(param, value))

def valid_input(param, value):
	# if email_address:
	# 	check that value follows '\w+[@]\w+[.]\w{3}' regex
	#	return true, value
	# if home_phone or mobile_phone:
	# 	check that value is 10 digits long
	#	return true, value
	# if mailing_address:
	#	turn value (dictionary) into Address
	# 	check that value has street, city, state, and zip
	#	return true, address
	# else:
	#	return false, value

def update_profile(param, value, user);
	if param == "mailing_address":
		user.mailing_address = value
	elif param == "home_phone":
		user.home_phone = value
	elif param == "mobile_phone":
		user.mobile_phone = value
	elif param == "email_address":
		user.email_address = value

	db.session.commit()

def error(status_code, error_message):
	return {'status': status_code, 'message': message}

api.add_resource(SavingsEndpoint, '/api/savings/<username>')
api.add_resource(CheckingEndpoint, '/api/checking/<username>')
api.add_resource(LoanEndpoint, '/api/loan/<username>')
api.add_resource(CertificateEndpoint, '/api/certificate/<username>')
api.add_resource(ProfileEndpoint, '/api/<username>')

class Address():

	def __init__(self, street, city, state, zipcode):
		self.street = street
		self.city = city
		self.state = state
		self.zipcode = zipcode

if __name__ == '__main__':
	app.run(debug=True)