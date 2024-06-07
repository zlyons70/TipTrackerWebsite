'''This file is used to define the different pages/views of the website'''
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Earning
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''Handles the logic for loading login page and logging in the user'''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # the below is how we look up a user in the database
        # .first() is used to get the first user that matches the query
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                # remembers that the user is logged in until the session is closed
                # this is how cookies are used to remember the user
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Username or Password Incorrect', category='error')
    return render_template('login.html', current_user=current_user)

@auth.route('/logout')
# Decorator requires user to be logged in to access this page
@login_required
def logout():
    '''Handles logout page'''
    # logs out the user
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    '''Handles logic for sign up page and creating a new user in the database'''
    if request.method == 'POST':
        # This will print the form data to the console
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 2 characters.', category='error')
        elif password != confirm_password:
            flash('Passwords do not match.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif User.query.filter_by(email=email).first():
            flash('Email is already in use.', category='error')
        elif User.query.filter_by(username=username).first():
            flash('Username is already in use.', category='error')
        else:
            # Below hashes the password to prevent it from being stored in plain text
            # note that this is a one way hash
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='scrypt'))
            # adds user to DB and commits the change
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created", category='success')
            login_user(new_user, remember=True)

            # once account is created redirect the user to the home page
            return redirect(url_for('views.home'))
    return render_template('signup.html', user=current_user)