from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config=None):

    app = Flask(__name__)
    if config is not None:
        app.config.from_object(config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'app_blue.login'
    
    with app.app_context():
        from flask_.views import app_blueprint
        app.register_blueprint(app_blueprint, url_prefix='/')
        db.create_all()

    return app