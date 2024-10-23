'''This file is used to define the different pages/views of the website'''
import json
from flask import Blueprint, request, jsonify
from .models import Earning, User
from .add_tips import add_tips

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


# @views.route('/viewtips', methods=['GET', 'POST'])
# def view_tips()->json:
#     '''This function is used to get the tips from the database'''
#     print("This is in views.py, handles the view tips page")
#     if request.method == 'GET':
#         data = request.json
#         user = data.get('username')
#         user = User.query.filter_by(username=user).first()
#         user_id = user.id
#         if not user_id:
#             return jsonify({'status': 'error', 'message': 'Not authenticated'})
#         return show_tips(data)






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
