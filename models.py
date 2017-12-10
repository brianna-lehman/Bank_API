from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy();

class Savings(db.Model):
	record_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(60), db.ForeignKey('profile.username'))
	description = db.Column(db.String(180), nullable=False)
	balance = db.Column(db.Float, nullable=False)
	last_activity = db.Column(db.DateTime, nullable=False)

	def __init__(self, username, description, balance, last_activity):
		self.username = username
		self.description = description
		self.balance = balance
		self.last_activity = last_activity

	def to_dict(self):
		return {'record_id':self.record_id, 'username':self.username, 'description':self.description, 'balance':self.balance, 'last_activity':self.last_activity.strftime('%m/%d/%Y')}

class Checking(db.Model):
	record_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(60), db.ForeignKey('profile.username'))
	description = db.Column(db.String(180), nullable=False)
	balance = db.Column(db.Float, nullable=False)
	last_activity = db.Column(db.DateTime, nullable=False)

	def __init__(self, username, description, balance, last_activity):
		self.username = username
		self.description = description
		self.balance = balance
		self.last_activity = last_activity

	def to_dict(self):
		return {'record_id':self.record_id, 'username':self.username, 'description':self.description, 'balance':self.balance, 'last_activity':self.last_activity.strftime('%m/%d/%Y')}

class Loan(db.Model):
	record_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(60), db.ForeignKey('profile.username'))
	description = db.Column(db.String(180), nullable=False)
	balance = db.Column(db.Float, nullable=False)
	last_activity = db.Column(db.DateTime, nullable=False)
	payment_due_date = db.Column(db.DateTime, nullable=False)
	minimum_amount_due = db.Column(db.Float, nullable=False)

	def __init__(self, username, description, balance, last_activity, payment_due_date, minimum_amount_due):
		self.username = username
		self.description = description
		self.balance = balance
		self.last_activity = last_activity
		self.payment_due_date = payment_due_date
		self.minimum_amount_due = minimum_amount_due

	def to_dict(self):
		return {'record_id':self.record_id, 'username':self.username, 'description':self.description, 'balance':self.balance, 'last_activity':self.last_activity.strftime('%m/%d/%Y'), 'payment_due_date':self.payment_due_date.strftime('%m/%d/%Y'), 'minimum_amount_due':self.minimum_amount_due}

class Certificate(db.Model):
	record_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(60), db.ForeignKey('profile.username'))
	description = db.Column(db.String(180), nullable=False)
	balance = db.Column(db.Float, nullable=False)
	last_activity = db.Column(db.DateTime, nullable=False)
	iterest_rate = db.Column(db.Float, nullable=True)
	maturity_date = db.Column(db.DateTime, nullable=False)

	def __init__(self, username, description, balance, last_activity, maturity_date, interest_rate=.05):
		self.username = username
		self.description = description
		self.balance = balance
		self.last_activity = last_activity
		self.interest_rate = interest_rate
		self.maturity_date = maturity_date

	def to_dict(self):
		return {'record_id':self.record_id, 'username':self.username, 'description':self.description, 'balance':self.balance, 'last_activity':self.last_activity.strftime('%m/%d/%Y'), 'interest_rate':self.interest_rate, 'maturity_date':self.maturity_date.strftime('%m/%d/%Y')}

class Profile(db.Model):
	record_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(60), nullable=False)
	name = db.Column(db.String(60), nullable=False)
	mailing_address = db.Column(db.PickleType, nullable=False)
	home_phone = db.Column(db.String(10), nullable=True)
	mobile_phone = db.Column(db.String(10), nullable=True)
	email_address = db.Column(db.String(40), nullable=False)

	def __init__(self, username, name, mailing_address, email_address, home_phone="", mobile_phone=""):
		self.username = username
		self.name = name
		self.mailing_address = mailing_address
		self.email_address = email_address
		self.home_phone = home_phone
		self.mobile_phone = mobile_phone

	def to_dict(self):
		return {'record_id':self.record_id, 'username':self.username, 'name':self.name, 'mailing_address':self.mailing_address.to_dict(), 'home_phone':self.home_phone, 'mobile_phone':self.mobile_phone, 'email_address':self.email_address}