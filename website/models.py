'''This file is used to handle the database of the website'''
from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    '''This class is used to define the user table in the database'''
    # Primary key is a unique identifier for each user
    id = db.Column(db.Integer, primary_key=True)