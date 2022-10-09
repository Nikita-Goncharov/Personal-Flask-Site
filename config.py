import os
from os.path import join, dirname
from dotenv import load_dotenv

BASE_DIR = join(dirname(__file__), '.env')
load_dotenv(BASE_DIR)



class DevConfig:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    # TESTING = True
    FLASK_ADMIN_SWATCH = 'cerulean'
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    CHAT_ID = os.environ.get('CHAT_ID')



class ProdConfig:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_ADMIN_SWATCH = 'cerulean'
    # TESTING = False