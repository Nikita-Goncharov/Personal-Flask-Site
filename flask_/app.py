from flask import Flask
from .main_module.views import blueprint as main_blueprint
from .auth_module.views import blueprint as auth_blueprint
from .extensions import db, toolbar, login_manager, admin


def register_extensions(app):
    db.init_app(app)
    toolbar.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'app_blue.login'
    admin.init_app(app)
    admin.name = 'Web on Python'
    admin.template_mode = 'bootstrap3'

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