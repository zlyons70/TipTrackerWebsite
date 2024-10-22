'''This file is used to define the different pages/views of the website'''
import json
from flask import Blueprint, request, jsonify, session
from .models import Earning, User
from .auth import get_current_user
from . import db
from datetime import datetime
from .get_tip_functions import get_tips_total, get_tips_month, get_tips_week, get_tips_day, get_tips_year
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home()->json:
    '''This function handles the logic of the home page'''
    print("This is in views.py, handles the home page")
    
    if request.method == 'POST':
        data = request.json
        user = data.get('username')
        print(data)
        return jsonify({'status': 'success', 'message': 'Data received', 'user': user})
    return jsonify({'status': 'error', 'message': 'Data not received'})
    # if request.method == 'POST':
    #     tip = float(request.form.get('tip'))
    #     get_date = request.form.get('date')
    #     if tip < 0:
    #         flash('Invalid Amount', category='error')
    #     else:
    #         new_earning = Earning(data=tip, date=datetime(year=int(get_date[0:4]), month=int(get_date[5:7]), day=int(get_date[8:10])), user_id=current_user.id)
    #         db.session.add(new_earning)
    #         db.session.commit()
    #         flash('Tip Logged Succesfully', category='success')
    
    # tips = get_tips_total()
    # print("here")
    # month = get_tips_month(5, 2023)
    # print(month)
    # print("below I'm testing the week function")
    # week = get_tips_week(5, 1, 7, 2023)
    # print(week)
    # return render_template('home.html', user=current_user, tips=tips)

@views.route('/addtips', methods=['GET', 'POST'])
def add_tips()->str:
    '''This function handles the logic of the add tips page'''
    
