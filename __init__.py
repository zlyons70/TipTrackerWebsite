from flask import Flask

def create_app():
    app = Flask(__name__)
    # all flask applications need a secret key
    app.config['SECRET_KEY'] = 'secret-key'
    