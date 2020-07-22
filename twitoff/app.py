import os
from flask_dotenv import DotEnv
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from .models import DB, User,Tweet, add_test_users
from .admin.routes import admin
from .main.routes import main

def create_app():                 # TODO add config from file
   app = Flask(__name__)  # create Flask instance
   Bootstrap(app)         # create bootstrap instance 
   env = DotEnv()
   env.init_app(app)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   
   app.register_blueprint(main)
   app.register_blueprint(admin)
   DB.init_app(app)       # db  instance setup
   return app

