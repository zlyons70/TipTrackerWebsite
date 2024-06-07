'''This file is used to define the different pages/views of the website'''
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Earning, User
from . import db
views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    '''This function is the home page of our url'''
    if request.method == 'POST':
        tip = request.form.get('tip')
        if len(tip) < 0:
            flash('Tip is too short!', category='error')
        else:
            new_earning = Earning(data=tip, user_id=current_user.id)
            db.session.add(new_earning)
            db.session.commit()
    return render_template('home.html', user=current_user)