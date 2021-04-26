
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from dotenv import load_dotenv
import os
load_dotenv('bearerToken.env')

# If you want the bearer token for the twitterAPI, ask Zoya. You need to make a bearerToken.env file in this directory 
# with the format BEARER_TOKEN="<thebearertoken>"


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    ENV = 'dev'
    if ENV == 'dev':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/'
        app.debug = True
        # Change the line below to your own local database for testing purposes

    else:
        app.debug = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI').replace("://", "ql://", 1)
    
    db.init_app(app)    
    
    from . import models


    with app.app_context():
        db.create_all()

    return app
