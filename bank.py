from flask_restful import reqparse, abort, fields, marshal_with, Api, Resource, request
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash, _app_ctx_stack
from models import db, Savings, Checking, Loan, Certificate, Profile
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import os
import re
import ast

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
	savings_one = Savings("cate38", "savings account for cate38", 1000.42, datetime.now())
	savings_two = Savings("leah223", "savings account for leah223", 583792.83, datetime.now())
	savings_three = Savings("marcia12", "savings account for marcia12", 100000, datetime.now())
	db.session.add(savings_one)
	db.session.add(savings_two)
	db.session.add(savings_three)

	checking_one = Checking("cate38", "checking account for cate38", 664839.38, datetime.now())
	checking_two = Checking("leah223", "checking account for leah223", 3829.33, datetime.now())
	checking_three = Checking("marcia12", "checking account for marcia12", 582.11, datetime.now())
	db.session.add(checking_one)
	db.session.add(checking_two)
	db.session.add(checking_three)

	loan_one = Loan("cate38", "loan for cate38", 100000, datetime.now(), datetime.now()+relativedelta(years=5), 500)
	loan_two = Loan("leah223", "loan for leah223", 1000, datetime.now(), datetime.now()+relativedelta(years=8), 500)
	loan_three = Loan("marcia12", "loan for marcia12", 500000, datetime.now(), datetime.now()+relativedelta(years=10), 1000)
	db.session.add(loan_one)
	db.session.add(loan_two)
	db.session.add(loan_three)

	# certificate_one = Certificate("cate38", "certificate for cate38", 1000, datetime.now(), datetime.now()+relativedelta(years=15))
	# certificate_two = Certificate("leah223", "certificate for leah223", 500, datetime.now(), datetime.now()+relativedelta(years=10))
	# certificate_three = Certificate("marcia12", "certificate for marcia12", 100000, datetime.now(), datetime.now()+relativedelta(years=20))
	# db.session.add(certificate_one)
	# db.session.add(certificate_two)
	# db.session.add(certificate_three)

	db.session.commit()

# "/savings/<username>"
class SavingsEndpoint(Resource):
	def get(self, username):
		# given username, get savings data for that user, return data as json
		saving_account = Savings.query.filter_by(username=username).first()
		if saving_account:
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
			return checking_account.to_dict()
		else:
			return error(400, "Checking doesn't exists under {}".format(username))

# "/loan/<username>"
class LoanEndpoint(Resource):
	def get(self, username):
		# given username, get loan data for that user, return data as json
		loan = Loan.query.filter_by(username=username).first()
		if loan:
			return loan.to_dict()
		else:
			return error(400, "Loan doesn't exists under {}".format(username))

# "/certificate/<username>"
# class CertificateEndpoint(Resource):
# 	def get(self, username):
# 		# given username, get certificate data for that user, return data as json
# 		certificate = Certificate.query.filter_by(username=username).first()
# 		if certificate:
# 			return certificate.to_dict()
# 		else:
# 			return error(400, "Certificate doesn't exists under {}".format(username))

# "/<username>"
class ProfileEndpoint(Resource):
	def get(self, username):
		# given username, get profile for that user, return data as json
		user = Profile.query.filter_by(username=username).first()
		if user:
			return user.to_dict()
		else:
			return error(400, "{} doesn't exist".format(username))

	# "/<username>?param=<param>&value=<value>"
	def put(self, username):
		parser = reqparse.RequestParser()
		parser.add_argument('param', type=str)
		parser.add_argument('value', type=str)

		args = parser.parse_args()
		print(args)
		param = args['param']
		value = args['value']

		input_is_valid, value = valid_input(param, value)
		if input_is_valid:
			user = Profile.query.filter_by(username=username).first()
			if user:
				# update value of param
				update_profile(param, value, user)
				user = Profile.query.filter_by(username=username).first()
				return user.to_dict()
			else:
				return error(400, "{} doesn't exist in the database".format(username))
		else:
			return error(400, "Param {} or value {} is invalid".format(param, value))

def valid_input(param, value):
	valid = True

	if param == "email_address":
		if not re.match("\w+[@]\w+[.]\w{3}", value):
			valid = False
	if param == "home_phone" or "mobile_phone":
		if len(value) != 10:
			valid = False
	if param == "mailing_address":
		value = ast.literal_eval(value)
		print("JSON "+str(value))
		if value['street'] and value['city'] and value['state'] and value['zipcode']:
			value = Address(value['street'], value['city'], value['state'], value['zipcode'])
			print("Address Object "+str(value.to_dict))
			valid = True
		else:
			valid = False

	return valid, value

def update_profile(param, value, user):
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
	return {'status': status_code, 'message': error_message}

api.add_resource(SavingsEndpoint, '/api/savings/<username>')
api.add_resource(CheckingEndpoint, '/api/checking/<username>')
api.add_resource(LoanEndpoint, '/api/loan/<username>')
# api.add_resource(CertificateEndpoint, '/api/certificate/<username>')
api.add_resource(ProfileEndpoint, '/api/<username>')

class Address():

	def __init__(self, street, city, state, zipcode):
		self.street = street
		self.city = city
		self.state = state
		self.zipcode = zipcode

	def to_dict(self):
		return {'street':self.street, 'city':self.city, 'state':self.state, 'zipcode':self.zipcode}

if __name__ == '__main__':
	app.run(debug=True)