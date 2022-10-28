from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
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