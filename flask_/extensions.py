from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from flask_admin import Admin

db = SQLAlchemy()
admin = Admin()
login_manager = LoginManager()
toolbar = DebugToolbarExtension()