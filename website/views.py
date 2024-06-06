'''This file is used to define the different pages/views of the website'''
from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    '''This function is the home page of our url'''
    return render_template('home.html')