from .models import Earning
from flask_login import current_user
from sqlalchemy.sql import func
'''EVERYTHING IS GROSS RIGHT NOW, FIX LATER'''
def get_tips_total(user_id: str)->list:
    '''Used to get all tips from a user'''
    earnings = Earning.query.filter_by(user_id=user_id).all()
    total = [earnings.gross for earnings in earnings]
    print("total", total)
    return total

def get_tips_month(month: int, year: int, user_id: str)->list:
    '''Used to get tips in current Month'''
    print("in get_tips_month")
    total_dict = {}
    total = []
    earnings = (Earning.query.filter_by(user_id=user_id)
                .filter(func.extract('month', Earning.date) == month)
                .filter(func.extract('year', Earning.date) == year)
                .all())
    # below is used to get the total tips for each day
    # this keeps in mind that there could be multiple tips in a day for doubles
    for earning in earnings:
        converted_date = earning.date.strftime("%Y-%m-%d")
        if converted_date in total_dict:
            total_dict[converted_date].append(earning.gross)
        else:
            total_dict[converted_date] = [earning.gross]
    for key in total_dict:
        total.append([key, sum(total_dict[key])])
    print("total", total)
    return total

def get_tips_year(year: int, user_id: str)->list:
    '''Used to get tips in current Year'''
    earnings = (Earning.query.filter_by(user_id=user_id)
                .filter(func.extract('year', Earning.date) == year)
                .all())
    total = [earnings.data for earnings in earnings]
    return total

def get_tips_day( month: int, day: int, year: int, user_id: str)->list:
    '''Used to get tips in current Day'''
    earnings = (Earning.query.filter_by(user_id=user_id)
                .filter(func.extract('day', Earning.date) == day)
                .filter(func.extract('month', Earning.date) == month)
                .filter(func.extract('year', Earning.date) == year)
                .all())
    total = [earnings.data for earnings in earnings]
    return total

def get_tips_week(month: int, start_day: int, end_day: int,  year: int, user_id: str)->list:
    '''Used to get tips of a selected week'''
    earnings = (Earning.query.filter_by(user_id=user_id)
                .filter(func.extract('year', Earning.date) == year)
                .filter(func.extract('month', Earning.date) == month)
                .filter(func.extract('day', Earning.date) >= start_day)
                .filter(func.extract('day', Earning.date) <= end_day))
    total = [earnings.data for earnings in earnings]
    return total
