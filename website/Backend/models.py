'''This file is used to handle the database of the website'''
from . import db

class Earning(db.Model):
    '''This class is used to define the earning table in the database'''
    __tablename__ = 'earning'
    id = db.Column(db.Integer, primary_key=True)
    job_class = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=False))
    declared_tips = db.Column(db.Float)
    cash_tips = db.Column(db.Float)
    hours_worked = db.Column(db.Float)
    food_sales = db.Column(db.Float)
    na_bev_sales = db.Column(db.Float)
    alcohol_sales = db.Column(db.Float)
    gross = db.Column(db.Float)
    net = db.Column(db.Float)
    # relationship between the user and the earnings
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='earnings')

class User(db.Model):
    '''This class is used to define the user table in the database'''
    __tablename__ = 'user'
    # Primary key is a unique identifier for each user
    id = db.Column(db.String(36), primary_key=True)
    # max string length is 150 and each email must be unique
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(255))
    username = db.Column(db.String(150), unique=True)
    # below is essentially a list of all earnings the user has created
    earnings = db.relationship('Earning', back_populates='user')
    # below is the user's settings
    # uselist=False means that there is only one setting per user
    user_settings = db.relationship('UserSettings', back_populates='user', uselist=False)

class UserSettings(db.Model):
    '''This class is used to define the user settings table in the database'''
    __tablename__ = 'user_settings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='user_settings')
    # below is the user's settings
    hourly_rate = db.Column(db.Float)
    taxes = db.Column(db.Float)
    # below is the user's settings
    user = db.relationship('User', back_populates='user_settings')