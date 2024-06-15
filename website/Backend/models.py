'''This file is used to handle the database of the website'''
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

class Earning(db.Model):
    '''This class is used to define the earning table in the database'''
    id = db.Column(db.Integer, primary_key=True)
    # the below data that our user will be storing is going to be the tip number
    data = db.Column(db.Float, nullable=False)
    # this automatically sets the date to the current date and time
    date = db.Column(db.DateTime(timezone=True))
    # This is a foreign key that is linked to the user table
    # this is used to link the note to the user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class User(db.Model, UserMixin):
    '''This class is used to define the user table in the database'''
    # Primary key is a unique identifier for each user
    id = db.Column(db.Integer, primary_key=True)
    # max string lenght is 150 and each email must be unique
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150), unique=True)
    # below is essentially a list of all earnings the user has created
    earning = db.relationship('Earning')