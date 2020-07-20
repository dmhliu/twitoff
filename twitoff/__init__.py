"""
Entry point for the Flask application 
"""

from flask import Flask
from flask import Blueprint
from .controllers import main
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

app.register_blueprint(main, url_prefix='/')
