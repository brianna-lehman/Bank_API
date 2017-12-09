from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy();

class Savings(db.Model):
	record_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(60), db.ForeignKey('profile.username'))
	description = db.Column(db.String(180), nullable=False)
	balance = db.Column(db.Float, nullable=False)
	last_activity = db.Column(db.DateTime, nullable=False)

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

class Profile(db.Model);
	record_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(60) nullable=False)
	name = db.Column(db.String(60), nullable=False)
	mailing_address = db.Column(Address, )
	home_phone
	mobile_phone
	email_address