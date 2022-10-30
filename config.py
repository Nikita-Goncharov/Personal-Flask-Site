import os
from os.path import join, dirname
from dotenv import load_dotenv

BASE_DIR = join(dirname(__file__), '.env')
load_dotenv(BASE_DIR)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    FLASK_ADMIN_SWATCH = 'cerulean'
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    CHAT_ID = os.environ.get('CHAT_ID')
    UPLOAD_FOLDER = os.getcwd() + '/flask_/static/upload'

class DevConfig(Config):
    DEBUG = True
    # TESTING = True

class ProdConfig(Config):
    DEBUG = False
    # TESTING = False