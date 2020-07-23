import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    TWITTER_API_KEY="buR7ZaXdML975jbgGyb7jfWNS"
    TWITTER_API_KEY_SECRET="W5Zv3DWVgBLRqJfyg0aC0wgTUPxPFiSdpksca3dgFDho5gXStx"
    BASILICA_KEY="ca5c6f72-190b-b94f-5c56-de256e635811"

class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URL="postgres://uvadxjadmevwsy:f833132af9efeab4c7cd43d60705464b730384dcbf8173a5d5a180fd947e0bb3@ec2-52-201-55-4.compute-1.amazonaws.com:5432/d8sgib3hpuoulo"

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    DATABASE_URL="sqlite:///db.sqlite3"


class TestingConfig(Config):
    TESTING = True
