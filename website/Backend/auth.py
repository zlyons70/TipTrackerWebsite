'''This file is used to define the different pages/views of the website'''
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_user, login_required, logout_user, current_user
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
        print("this print statement is for debugging and workd")
        if user:
            if check_password_hash(user.password, password):
                print('Logged in successfully')
                token = jwt.encode({
                    'username': user.username,
                    'exp': 900,
                }, secret_key, algorithm='HS256')
                # remembers that the user is logged in until the session is closed
                # this is how cookies are used to remember the user
                login_user(user, remember=True)
                return jsonify({'status': 'success', 
                                'message': 'Logged in successfully',
                                'token': token})
            else:
               return jsonify({'status': 'error', 'message': 'Incorrect Username or Password'})
    return jsonify({'status': 'error', 'message': 'Incorrect Username or Password'})

@auth.route('/logout')
# Decorator requires user to be logged in to access this page
@login_required
def logout()->str:
    '''Handles logout page'''
    # logs out the user
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up()->str:
    '''Handles logic for sign up page and creating a new user in the database'''
    if request.method == 'POST':
        data = request.json
        # This will print the form data to the console
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
            # creates a token for the user
            # for this session to be valid for 15 minutes
            token = jwt.encode({
                    'username': new_user.username,
                    'exp': 900,
                }, secret_key, algorithm='HS256')
            login_user(new_user, remember=True)

            # once account is created redirect the user to the home page
            return jsonify({'status': 'success', 
                                'message': 'Account Created!',
                                'token': token})
    return render_template('signup.html', user=current_user)

@auth.route('/protected')
@login_required
def protected():
    '''This is a protected route that requires the user to be logged in'''
    return jsonify({'status': 'success', 'message': 'You are logged in'})
