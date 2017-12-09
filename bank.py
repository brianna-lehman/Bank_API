from flask_restful import reqparse, abort, fields, marshal_with, Api, Resource, request
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash, _app_ctx_stack

app = Flask(__name__)
api = Api(app)

def valid_input(param, value):
	# check that param == mailing_address, home_phone, mobile_phone, or email_address
	# if email_address:
	# 	check that value follows '+@+.+' regex
	# if home_phone or mobile_phone:
	# 	check that value is 10 digits long
	# if mailing_address:
	# 	check that value has stree, city, state, and zip

"/savings/<username>"
class Savings(Resource):
	def get(self, username):
		# given username, get savings data for that user, return data as json

"/checking/<username>"
class Checking(Resource):
	def get(self, username):
		# given username, get checking data for that user, return data as json

"/loan/<username>"
class Loan(Resource):
	def get(self, username):
		# given username, get loan data for that user, return data as json

"/certificate/<username>"
class Certificate(Resource):
	def get(self, username):
		# given username, get certificate data for that user, return data as json

"/<username>"
class Profile(Resource):
	def get(self, username):
		# given username, get savings profile for that user, return data as json

	"/<username>?param=<param>&value=value"
	def put(self, username):
		input_data = request.args.to_dict()
		param = input_data['param']
		value = input_data['value']
		if valid_input(param, value):
			# get the username profile data
			# update value of param
			# return profile data for that user
		else:
			# return error

api.add_resource(Savings, '/api/savings/<username>')
api.add_resource(Checking, '/api/checking/<username>')
api.add_resource(Loan, '/api/loan/<username>')
api.add_resource(Certificate, '/api/certificate/<username>')
api.add_resource(Profile, '/api/<username>')