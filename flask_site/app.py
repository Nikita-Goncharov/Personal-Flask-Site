import json

from flask import Flask, session, redirect, url_for
from flask_admin import BaseView, expose, AdminIndexView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from .auth_module.models import User
from .auth_module.views import blueprint as auth_blueprint
from .extensions import db, toolbar, login_manager, admin
from .main_module.models import Comment, Service, TechSkill, WorkExperience, TelegramAdmin, ShopBasket
from .main_module.views import blueprint as main_blueprint


class MyAdminView(AdminIndexView):
    @expose('/')
    def index(self):
        return super(MyAdminView, self).index()

    def is_accessible(self):
        return session.get('is_logged') and current_user.is_admin


class ImageView(FileAdmin):
    allowed_extensions = ('jpeg', 'png', 'jpg')

    def is_accessible(self):
        return session.get('is_logged') and current_user.is_admin


class MyModelView(ModelView):
    def is_accessible(self):
        return session.get('is_logged') and current_user.is_admin


class LogoutAdminView(BaseView):
    @expose('/')
    def logout_admin(self):
        return redirect(url_for('auth_blue.logout'))

    def is_accessible(self):
        return session.get('is_logged') and current_user.is_admin


def register_extensions(app):
    db.init_app(app)
    if app.config['DEBUG']:
        toolbar.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'auth_blue.login'
    admin.init_app(app, index_view=MyAdminView())
    admin.name = 'Web on Python'
    admin.template_mode = 'bootstrap3'
    admin.add_view(MyModelView(User, db.session))
    admin.add_view(MyModelView(Comment, db.session))
    admin.add_view(MyModelView(TechSkill, db.session))
    admin.add_view(MyModelView(WorkExperience, db.session))
    admin.add_view(MyModelView(TelegramAdmin, db.session))
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

        with open("admin_data.json", "r") as file:
            json_dict = json.load(file)
            name = json_dict.get("name", "Admin")
            email = json_dict.get("email", "admin@gmail.com")
            is_admin = json_dict.get("is_admin", False)
            password = json_dict.get("password", "12345678")
            is_user_exists = User.query.filter_by(email=email)
            if is_user_exists.count() == 0:
                admin_user = User(name=name, email=email)
                basket = ShopBasket()
                db.session.add(basket)
                db.session.commit()
                admin_user.is_admin = is_admin
                admin_user.basket_id = basket.id
                admin_user.set_password(password)
                db.session.add(admin_user)
                db.session.commit()

    return app
