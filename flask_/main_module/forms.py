from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField, PasswordField, FileField
from wtforms.validators import DataRequired, EqualTo, Email, Length

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=5)])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(min=8)])
    password1 = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Password repeat', validators=[DataRequired(), EqualTo('password1'), Length(min=6)])
    register = SubmitField('Register')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(min=8)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    login = SubmitField('Login')


class CommentForm(FlaskForm):
    client_name = StringField('Name', render_kw={'placeholder': 'Your name'}, validators=[DataRequired(message='This field must be filled')])
    message = TextAreaField('Message', render_kw={'placeholder': 'Comment'}, validators=[DataRequired(message='This field must be filled')])
    # add = SubmitField('Add comment')


class ContactForm(FlaskForm):
    name = StringField('Name', render_kw={'placeholder': 'Name'}, validators=[DataRequired(message='This field must be filled')])
    email = EmailField('Email', render_kw={'placeholder': 'Email'}, validators=[DataRequired(message='This field must be filled'), Email(message='Wrong email')])
    message = TextAreaField('Message', render_kw={'placeholder': 'Message'},  validators=[DataRequired(message='This field must be filled')])
    # send = SubmitField('Send')

class ServiceForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(message='This field must be filled')])
    description = TextAreaField('Description', validators=[DataRequired(message='This field must be filled')])
    logo = FileField('Logo')