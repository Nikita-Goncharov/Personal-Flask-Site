import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(__file__)
ENV_DIR = os.path.join(BASE_DIR, '.env')
load_dotenv(ENV_DIR)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    FLASK_ADMIN_SWATCH = 'cerulean'
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    CHAT_ID = os.environ.get('CHAT_ID')
    UPLOAD_FOLDER = BASE_DIR + '/flask_/static/upload'

class DevConfig(Config):
    DEBUG = True
    # TESTING = True

class ProdConfig(Config):
    DEBUG = False
    # TESTING = False
