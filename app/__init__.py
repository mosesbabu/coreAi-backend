from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import config_options

db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__)

    
    
    #Initializing Flask Extensions
    db.init_app(app)
   
    return app
   
 