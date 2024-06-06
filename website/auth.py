'''This file is used to define the different pages/views of the website'''
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''Login Page'''
    data = request.form
    return render_template('login.html', boolean=True)

@auth.route('/logout')
def logout():
    '''Handles logout page'''
    return "<p>Logout Page</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    '''Handles sign up page'''
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
        else:
            flash("Account Created", category='success')
            # add user to the database
    return render_template('signup.html')