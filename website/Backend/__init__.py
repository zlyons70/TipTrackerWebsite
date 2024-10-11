from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
from flask_login import LoginManager
# below is used to connect to the mysql database
import mysql.connector
import os

load_dotenv()
db = SQLAlchemy()
# Constants for databases
DB_NAME = "test_db"
secret_key = os.getenv('SECRET_KEY')
MYSQL_CONNECTION = os.getenv('mysql_connection')
MYSQL_PASSWORD = os.getenv('mysql_password')

def create_app()->Flask:
    '''Initialize Flask application and return app object'''
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL_CONNECTION
    db.init_app(app)
    
    # once blueprints are defined we need to tell the flask server to use them
    from .views import views
    from .auth import auth
    # registers the blueprints, url prefix is the url that the blueprint will be accessed from
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Earning
    create_database(app)
    
    # if the user is not logged in it redirects them to the login page
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id)->User:
        '''This function is used to load the user from the database'''
        # Tells flask what user we're looking for
        return User.query.get(int(id))
    
    return app

def create_database(app)->None:
    '''Create the database if it does not exist'''
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=MYSQL_PASSWORD,)
    # see if the database exists
    mycursor = mydb.cursor()
    print("showing databases command")
    mycursor.execute("SHOW DATABASES LIKE 'test_db'")
    result = mycursor.fetchone()
    print(result)
    if not result:
        mycursor.execute("CREATE DATABASE test_db")
        print("Database Created")
    else:
        print("Database already exists")
    return None

def delete_database(app)->None:
    '''Delete the database if it exists'''
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=MYSQL_PASSWORD,)
    # see if the database exists
    mycursor = mydb.cursor()
    print("showing databases command")
    mycursor.execute("SHOW DATABASES LIKE 'test_db'")
    result = mycursor.fetchone()
    print(result)
    if result:
        mycursor.execute("DROP DATABASE test_db")
        print("Database Deleted")
    else:
        print("Database does not exist")