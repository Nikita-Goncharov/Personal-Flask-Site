from datetime import date
from flask_ import db, login_manager, admin
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from flask_admin.contrib.sqla import ModelView

class User(db.Model, UserMixin):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(150))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# class Service(db.Model):
#     __tablename__ = 'Services'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), unique=True)
#     photo = db.Column()
#     description = db.Column(db.Text)


class Comment(db.Model):
    __tablename__ = 'Comments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    time = db.Column(db.String(100), default=date.today().strftime("%B %d, %Y"))
    message = db.Column(db.Text)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Comment, db.session))