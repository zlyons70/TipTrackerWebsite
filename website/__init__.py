from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
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
    return app