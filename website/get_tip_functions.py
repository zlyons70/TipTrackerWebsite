from .models import Earning
from flask_login import current_user
from sqlalchemy.sql import func

def get_tips_total()->list:
    '''Used to get all tips from a user'''
    earnings = Earning.query.filter_by(user_id=current_user.id).all()
    total = [earnings.data for earnings in earnings]
    return total

def get_tips_month(month: int, year: int)->list:
    '''Used to get tips in current Month'''
    total = []
    earnings = (Earning.query
                .filter_by(user_id=current_user.id)
                .filter(func.extract('month', Earning.date) == month)
                .filter(func.extract('year', Earning.date) == year)
                .all())
    total = [earnings.data for earnings in earnings]
    return total

def get_tips_year(year: int)->list:
    '''Used to get tips in current Year'''
    earnings = (Earning.query.filter_by(user_id=current_user.id)
                .filter(func.extract('year', Earning.date) == year)
                .all())
    total = [earnings.data for earnings in earnings]
    return total

def get_tips_day( month: int, day: int, year: int)->list:
    '''Used to get tips in current Day'''
    earnings = (Earning.query.filter_by(user_id=current_user.id)
                .filter(func.extract('day', Earning.date) == day)
                .filter(func.extract('month', Earning.date) == month)
                .filter(func.extract('year', Earning.date) == year)
                .all())
    total = [earnings.data for earnings in earnings]
    return total

def get_tips_week(month: int, start_day: int, end_day: int,  year: int)->list:
    '''Used to get tips of a selected week'''
    earnings = (Earning.query.filter_by(user_id=current_user.id)
                .filter(func.extract('year', Earning.date) == year)
                .filter(func.extract('month', Earning.date) == month)
                .filter(func.extract('day', Earning.date) >= start_day)
                .filter(func.extract('day', Earning.date) <= end_day))
    total = [earnings.data for earnings in earnings]
    return total
