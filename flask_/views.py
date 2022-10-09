from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from flask_.forms import CommentForm, RegisterForm, LoginForm, ContactForm
from flask_.models import User, Comment
from flask_ import db
from .send_msg_bot import send_msg_bot
from datetime import date

app_blueprint = Blueprint('app_blue', __name__, static_folder='static',
                        template_folder='templates', static_url_path='')


@app_blueprint.route('/', methods=['GET', 'POST'])
def index():
    comment_form = CommentForm()
    contact_form = ContactForm()
    comments = Comment.query.all()

    if comment_form.validate_on_submit():
        name=comment_form.client_name.data
        message=comment_form.message.data
        time=date.today().strftime("%B %d, %Y")
        comment = Comment(name=name, message=message)# , time=time     , time=date.today().strftime("%B %d, %Y")
        send_msg_bot(name=name, message=message, time=time, type_of_message='contact')
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('app_blue.index'))

    if contact_form.validate_on_submit():
        name=contact_form.name.data
        email=contact_form.email.data
        message=contact_form.message.data
        contact = ContactForm(name=name, email=email, message=message)
        send_msg_bot(name=name, email=email, message=message, type_of_message='contact')
        return redirect(url_for('app_blue.index'))
    return render_template('flask_/home.html', comment_form=comment_form, contact_form=contact_form, comments=comments)


@app_blueprint.route('/resume')
def resume():
    return render_template('flask_/resume.html')


@app_blueprint.route('/services')
def services():
    return render_template('flask_/service.html')


@app_blueprint.route('/about')
def about():
    return render_template('flask_/about.html')


@app_blueprint.route('/contact', methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        name=contact_form.name.data
        email=contact_form.email.data
        message=contact_form.message.data
        contact = ContactForm(name=name, email=email, message=message)
        send_msg_bot(name=name, email=email, message=message, type_of_message='contact')
        return redirect(url_for('app_blue.index'))
    return render_template('flask_/contact.html', contact_form=contact_form)


@app_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        user = User(name=name, email=email)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('app_blue.index'))
    return render_template('auth/register.html', form=form)


@app_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('app_blue.index'))
        return redirect(url_for('app_blue.login'))
    return render_template('auth/login.html', form=form)


@app_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('app_blue.login'))