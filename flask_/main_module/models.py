from datetime import date
from flask_.extensions import db


class Service(db.Model):
    __tablename__ = 'Services'
    id = db.Column(db.Integer, primary_key=True)
    service_title = db.Column(db.String(30))
    description = db.Column(db.Text)
    filename = db.Column(db.String(100))


class Comment(db.Model):
    __tablename__ = 'Comments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    time = db.Column(db.String(100), default=date.today().strftime("%B %d, %Y"))
    message = db.Column(db.Text)


