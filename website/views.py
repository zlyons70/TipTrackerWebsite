'''This file is used to define the different pages/views of the website'''
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Earning
from . import db
from datetime import datetime
from sqlalchemy.sql import func

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home()->str:
    '''This function handles the logic of the home page'''
    if request.method == 'POST':
        tip = float(request.form.get('tip'))
        get_date = request.form.get('date')
        if tip < 0:
            flash('Invalid Amount', category='error')
        else:
            new_earning = Earning(data=tip, date=datetime(year=int(get_date[0:4]), month=int(get_date[5:7]), day=int(get_date[8:10])), user_id=current_user.id)
            db.session.add(new_earning)
            db.session.commit()
            flash('Tip Logged Succesfully', category='success')
    
    tips = get_tips_total()
    print("here")
    month = get_tips_month()
    print(month)
    
    return render_template('home.html', user=current_user, tips=tips)

def get_tips_total()->list:
    '''Used to get all tips from a user'''
    earnings = Earning.query.filter_by(user_id=current_user.id).all()
    total = [earnings.data for earnings in earnings]
    return total

#TODO: Implement ability for user to input the month they want to view
def get_tips_month()->list:
    '''Used to get tips in current Month'''
    total = []
    current_month = datetime.now().month
    earnings = (Earning.query
                .filter_by(user_id=current_user.id)
                .filter(func.extract('month', Earning.date) == current_month)
                .all())
    total = [earnings.data for earnings in earnings]
    return total

# TODO: Implement ability for user to input the year they want to view
def get_tips_year()->list:
    '''Used to get tips in current Year'''
    current_year = datetime.now().year
    earnings = (Earning.query.filter_by(user_id=current_user.id)
                .filter(func.extract('year', Earning.date) == current_year)
                .all())
    total = [earnings.data for earnings in earnings]
    return total
