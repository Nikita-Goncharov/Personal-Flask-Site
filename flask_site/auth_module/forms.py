from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email, Length

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=5)], render_kw={"placeholder": "Name"})
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(min=8)], render_kw={"placeholder": "Email"})
    password1 = PasswordField('Password', validators=[DataRequired(), Length(min=6)], render_kw={"placeholder": "Password"})
    password2 = PasswordField('Password repeat', validators=[DataRequired(), EqualTo('password1'), Length(min=6)], render_kw={"placeholder": "Repeat password"})

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(min=8)], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)], render_kw={"placeholder": "Password"})