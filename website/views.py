'''This file is used to define the different pages/views of the website'''
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Earning
from . import db
views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home()->str:
    '''This function is the home page of our url'''
    if request.method == 'POST':
        tip = request.form.get('tip')
        if int(tip) < 0:
            flash('Invalid Amount', category='error')
        else:
            new_earning = Earning(data=tip, user_id=current_user.id)
            db.session.add(new_earning)
            db.session.commit()
            flash('Tip Added', category='success')
    tips = get_tips()
    return render_template('home.html', user=current_user, tips=tips)

def get_tips()->list:
    '''Used to get all tips from a user'''
    earnings = Earning.query.filter_by(user_id=current_user.id).all()
    total = []
    for earnings in earnings:
        total.append(earnings.data)
    return total
