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

class Loan(db.Model):
	record_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(60), db.ForeignKey('profile.username'))
	description = db.Column(db.String(180), nullable=False)
	balance = db.Column(db.Float, nullable=False)
	last_activity = db.Column(db.DateTime, nullable=False)
	payment_due_date = db.Column(db.DateTime, nullable=False)
	minimum_amount_due = db.Column(db.Float, nullable=False)

class Certificate(db.Model):
	record_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(60), db.ForeignKey('profile.username'))
	description = db.Column(db.String(180), nullable=False)
	balance = db.Column(db.Float, nullable=False)
	last_activity = db.Column(db.DateTime, nullable=False)
	iterest_rate = db.Column(db.Float, nullable=False)
	maturity_date = db.Column(db.DateTime, nullable=False)

class Profile(db.Model):
	record_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(60), nullable=False)
	name = db.Column(db.String(60), nullable=False)
	mailing_address = db.Column(db.PickleType, nullable=False)
	home_phone = db.Column(db.String(10), nullable=True)
	mobile_phone = db.Column(db.String(10), nullable=True)
	email_address = db.Column(db.String(40), nullable=False)

	def __init__(self, username, name, mailing_address, email_address, home_phone=None, mobile_phone=None):
		self.username = username
		self.name = name
		self.mailing_address = mailing_address
		self.email_address = email_address
		self.home_phone = home_phone
		self.mobile_phone = mobile_phone