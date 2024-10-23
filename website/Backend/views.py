'''This file is used to define the different pages/views of the website'''
import json
from flask import Blueprint, request, jsonify
from .models import Earning, User
from . import db
from datetime import datetime
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
        show_tips(data)
        return add_tips(data)
    return jsonify({'status': 'error', 'message': 'Data not received'})

def add_tips(data:json) -> json:
    '''This function is used to add tips to the database'''
    username = data.get('username')
    # with username pull user from database
    print("in add_tips")
    print("username", username)
    
    user= User.query.filter_by(username=username).first()
    print("user", user)
    job_class = data.get('jobClass')
    
    declared_tips = data.get('declaredTips')
    declared_tips = float(declared_tips)
    
    cash_tips = data.get('cashTips')
    cash_tips = float(cash_tips)
    
    food_sales = float(data.get('foodSales') or 0)
    na_bev_sales = float(data.get('naBevSales') or 0)
    alcohol_sales = float(data.get('alcoholSales') or 0)
    
    date = data.get('date')
    converted_date = datetime(year=int(date[0:4]), month=int(date[5:7]), day=int(date[8:10]))
    
    if user:
        try:
            new_earning = Earning(job_class=job_class, date=converted_date, declared_tips=declared_tips, 
                                cash_tips=cash_tips, food_sales=food_sales, na_bev_sales=na_bev_sales, 
                                alcohol_sales=alcohol_sales, user_id=user.id)
            db.session.add(new_earning)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Tips added successfully', 'user': username})
        except Exception as e:
            db.session.rollback()
            return jsonify({'status': 'error', 'message': 'Tips not added', 'error': str(e)})
    return jsonify({'status': 'error', 'message': 'User not found'})

def show_tips(data:json) -> json:
    '''This function is used to show the tips in the database'''
    username = data.get('username')
    user = User.query.filter_by(username=username).first()
    if user:
        earnings = Earning.query.filter_by(user_id=user.id).all()
        for earning in earnings:
            print(earning.job_class, earning.date, earning.declared_tips, earning.cash_tips, earning.food_sales, earning.na_bev_sales, earning.alcohol_sales)
        return jsonify({'status': 'success', 'message': 'Tips found'})
    return jsonify({'status': 'error', 'message': 'User not found'})
