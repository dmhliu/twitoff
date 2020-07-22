#!/ usr/bin/env python
# this file indicates we are in a twitoff package folder. 

from .app import create_app

APP = create_app()  # create an instance of the app, a global 

