import os
from os import getenv 
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from .models import DB, User,Tweet, add_test_users
from .twitter import add_or_update_user, add_users, update_all_users
from .predict import predict_user
from .admin.routes import admin
from .main.routes import main

def create_app():                 # TODO add config from file
   app = Flask(__name__)  # create Flask instance
   Bootstrap(app)         # create bootstrap instance 
   app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   
   app.register_blueprint(main)
   app.register_blueprint(admin)
   DB.init_app(app)       # db  instance setup
   return app

