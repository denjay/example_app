import os

DEBUG = True
SECRET_KEY = 'ding'
SQLALCHEMY_TRACK_MODIFICATIONS = True
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
