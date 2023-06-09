from flask import session
from flask_admin import Admin, AdminIndexView
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


class MyAdminView(AdminIndexView):
    def is_accessible(self):
        return session.get('is_logged')

    def is_visible(self):
        return False


db = SQLAlchemy()
admin = Admin(index_view=MyAdminView())
login_manager = LoginManager()
toolbar = DebugToolbarExtension()
