from flask import Flask, session, redirect, url_for
from flask_admin import BaseView, expose
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView

from .auth_module.models import User
from .auth_module.views import blueprint as auth_blueprint
from .extensions import db, toolbar, login_manager, admin
from .main_module.models import Comment, Service, TechSkill, WorkExperience
from .main_module.views import blueprint as main_blueprint


class ImageView(FileAdmin):
    allowed_extensions = ('jpeg', 'png', 'jpg')

    def is_accessible(self):
        return session.get('is_logged')


class MyModelView(ModelView):
    def is_accessible(self):
        return session.get('is_logged')


class LogoutAdminView(BaseView):
    @expose('/')
    def logout_admin(self):
        return redirect(url_for('auth_blue.logout'))


def register_extensions(app):
    db.init_app(app)
    if app.config['DEBUG']:
        toolbar.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'auth_blue.login'
    admin.init_app(app)
    admin.name = 'Web on Python'
    admin.template_mode = 'bootstrap3'
    admin.add_view(MyModelView(User, db.session))
    admin.add_view(MyModelView(Comment, db.session))
    admin.add_view(MyModelView(TechSkill, db.session))
    admin.add_view(MyModelView(WorkExperience, db.session))
    admin.add_view(MyModelView(Service, db.session, category='Service'))
    admin.add_view(ImageView(app.config['UPLOAD_FOLDER'], name='Upload image for service', category='Service'))
    admin.add_view(LogoutAdminView(name='Logout', endpoint='logout'))


def register_blueprints(app):
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    with app.app_context():
        # db.drop_all()
        db.create_all()

    return app
