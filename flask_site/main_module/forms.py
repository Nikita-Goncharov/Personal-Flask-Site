from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, FileField
from wtforms.validators import DataRequired, Email


class CommentForm(FlaskForm):
    client_name = StringField('Name', render_kw={'placeholder': 'Your name'}, validators=[DataRequired(message='This field must be filled')])
    message = TextAreaField('Message', render_kw={'placeholder': 'Comment'}, validators=[DataRequired(message='This field must be filled')])

class ContactForm(FlaskForm):
    name = StringField('Name', render_kw={'placeholder': 'Name'}, validators=[DataRequired(message='This field must be filled')])
    email = EmailField('Email', render_kw={'placeholder': 'Email'}, validators=[DataRequired(message='This field must be filled'), Email(message='Wrong email')])
    message = TextAreaField('Message', render_kw={'placeholder': 'Message'},  validators=[DataRequired(message='This field must be filled')])

class ServiceForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(message='This field must be filled')])
    description = TextAreaField('Description', validators=[DataRequired(message='This field must be filled')])
    logo = FileField()