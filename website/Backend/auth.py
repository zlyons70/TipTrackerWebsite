'''This file is used to define the different pages/views of the website'''
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify, session
from flask_login import login_user, logout_user, current_user
from .models import User, Earning
import jwt, json, os
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from dotenv import load_dotenv

load_dotenv()
secret_key = os.getenv('SECRET_KEY')
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login()->json:
    '''Handles the logic for loading login page and logging in the user'''
    if request.method == 'POST':
        data = request.json
        username = data.get('username')
        password = data.get('password')
        # the below is how we look up a user in the database
        # .first() is used to get the first user that matches the query
        user = User.query.filter_by(username=username).first()
        print("This is in auth.py, handles the login page")
        print("this print statement is for debugging")
        if user:
            if check_password_hash(user.password, password):
                print('Logged in successfully')
                print("logged in")
                session['user_id'] = user.id
                return jsonify({'status': 'success', 
                                'message': 'Logged in successfully'})
            else:
               return jsonify({'status': 'error', 'message': 'Incorrect Username or Password'}), 401
    return jsonify({'status': 'error', 'message': 'Incorrect Username or Password'}), 401

@auth.route('/logout', methods = ['POST'])
def logout()->json:
    '''Handles logout button'''
    session.pop('user_id', None)
    return jsonify({'status': 'success', 'message': 'Logged out successfully'})

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up()->json:
    '''Handles logic for sign up page and creating a new user in the database'''
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        print(email, username, password, confirm_password)
        # below are the checks required to create an account
        if len(email) < 4:
            return jsonify({'status': 'error', 'message': 'Email must be greater than 4 characters.'})
        elif len(username) < 2:
            return jsonify({'status': 'error', 'message': 'Username must be greater than 2 characters.'})
        elif password != confirm_password:
            return jsonify({'status': 'error', 'message': 'Passwords do not match.'})
        elif len(password) < 7:
            return jsonify({'status': 'error', 'message': 'Password must be at least 7 characters.'})
        elif User.query.filter_by(email=email).first():
            return jsonify({'status': 'error', 'message': 'Email is already in use.'})
        elif User.query.filter_by(username=username).first():
            return jsonify({'status': 'error', 'message': 'Username is already in use.'})
        else:
            # Below hashes the password to prevent it from being stored in plain text
            # note that this is a one way hash
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='scrypt'))
            # adds user to DB and commits the change
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            # once account is created redirect the user to the home page
            return jsonify({'status': 'success', 
                                'message': 'Account Created!'})

@auth.route('/@me')
def get_current_user()->json:
    '''This function is used to get the current user'''
    user_id = session.get('user_id')
    print("got called")
    if not user_id:
        print("User not found")
        return jsonify({'status': 'error', 'message': 'User not found'}), 401
    user = User.query.get(user_id)
    if user:
        print("User found")
        return jsonify({'status': 'success', 'message': 'User found', 'user': user.username}), 200