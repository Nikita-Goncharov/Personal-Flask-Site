from datetime import date
from flask_.extensions import db, admin
from flask_admin.contrib.sqla import ModelView


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


admin.add_view(ModelView(Comment, db.session))