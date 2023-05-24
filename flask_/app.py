from flask import Flask
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView

from .auth_module.models import User
from .auth_module.views import blueprint as auth_blueprint
from .extensions import db, toolbar, login_manager, admin
from .main_module.models import Comment, Service
from .main_module.views import blueprint as main_blueprint


class ImageView(FileAdmin):
    allowed_extensions = ('jpeg', 'png', 'jpg')


def register_extensions(app):
    db.init_app(app)
    if app.config['DEBUG']:
        toolbar.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'app_blue.login'
    admin.init_app(app)
    admin.name = 'Web on Python'
    admin.template_mode = 'bootstrap3'
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Comment, db.session))
    admin.add_view(ModelView(Service, db.session, category='Service'))
    admin.add_view(ImageView(app.config['UPLOAD_FOLDER'], name='Upload image for service', category='Service'))


def register_blueprints(app):
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    with app.app_context():
        db.create_all()

    return app
