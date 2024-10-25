'''This file is used to define the different pages/views of the website'''
import json
from flask import Blueprint, request, jsonify
from .models import Earning, User
from .add_tips import add_tips
from .get_tip_functions import get_tips_total, get_tips_month, get_tips_year, get_tips_day, get_tips_week

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home()->json:
    '''This function handles the logic of the home page'''
    print("This is in views.py, handles the home page")
    if request.method == 'POST':
        data = request.json
        user = data.get('username')
        user = User.query.filter_by(username=user).first()
        user_id = user.id
        if not user_id:
            return jsonify({'status': 'error', 'message': 'Not authenticated'})
        # show_tips(data)
        return add_tips(data)
    return jsonify({'status': 'error', 'message': 'Data not received'})


@views.route('/viewtips', methods=['GET', 'POST'])
def view_tips()->json:
    '''This function is used to get the tips from the database'''
    print("This is in views.py, handles the view tips page")
    if request.method == 'POST':
        data = request.json
        user = data.get('username')
        user = User.query.filter_by(username=user).first()
        print("user", user.id)
        user_id = user.id
        date = data.get('date')
        time = data.get('time')
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:10])
        if not user_id:
            return jsonify({'status': 'error', 'message': 'Not authenticated'})
        if time == 'month':
            # get Month
            print("in month")
            return jsonify({'status': 'success', 'message': 'Month tips', 'data': get_tips_month(month, year, user_id)})
        if time =='week':
            # get Week
            start_day = data.get('start_day')
            end_day = data.get('end_day')
            return jsonify({'status': 'success', 'message': 'Week tips', 'data': get_tips_week(month, start_day, end_day, year, user_id)})
        if time == 'day':
            # get Day
            return jsonify({'status': 'success', 'message': 'Day tips', 'data': get_tips_day(month, day, year, user_id)})
        if time == 'total':
            # get Total
            return jsonify({'status': 'success', 'message': 'Total tips', 'data': get_tips_total(user_id)})
        if time == 'year':
            # get Year
            return jsonify({'status': 'success', 'message': 'Year tips', 'data': get_tips_year(year, user_id)})

    return jsonify({'status': 'error', 'message': 'Data not received'})


def show_tips(data:json) -> json:
    '''This function is used to show the tips in the database'''
    username = data.get('username')
    user = User.query.filter_by(username=username).first()
    print("in show_tips")
    if user:
        earnings = Earning.query.filter_by(user_id=user.id).all()
        for earning in earnings:
            print("here2")
            print(earning.job_class, earning.date, earning.declared_tips, earning.cash_tips, earning.food_sales, earning.na_bev_sales, earning.alcohol_sales, earnings.gross, earnings.net, earnings.hours_worked)
        return jsonify({'status': 'success', 'message': 'Tips found'})
    return jsonify({'status': 'error', 'message': 'User not found'})
