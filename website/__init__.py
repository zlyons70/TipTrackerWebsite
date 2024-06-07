from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_login import LoginManager
import os

load_dotenv()
db = SQLAlchemy()
DB_NAME = "database.db"
secret_key = os.getenv('SECRET_KEY')

def create_app():
    '''Initialize Flask application and return app object'''
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'SECRET_KEY'
    # Tell flask where the database is located
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # Initialize the database
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
    def load_user(id):
        '''This function is used to load the user from the database'''
        # Tells flask what user we're looking for
        return User.query.get(int(id))
    
    return app

def create_database(app):
    '''Create the database if it does not exist'''
    if not os.path.exists('instance/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Database Created")
    print("Database already exists!")
    return