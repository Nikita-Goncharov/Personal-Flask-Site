from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from flask_.forms import CommentForm, RegisterForm, LoginForm
from flask_.models import User, Comment
from flask_ import db
from datetime import date
app_blueprint = Blueprint('app_blue', __name__, static_folder='static', template_folder='templates', static_url_path='')


@app_blueprint.route('/', methods=['GET', 'POST'])
def index():
    form = CommentForm()
    comments = Comment.query.all()
    if form.validate_on_submit():
        comment = Comment(name=form.client_name.data, message=form.message.data, time=date.today().strftime("%B %d, %Y"))
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('app_blue.index'))
    return render_template('flask_/home.html', form=form, comments=comments)

@app_blueprint.route('/resume')
def resume():
    return render_template('flask_/resume.html')

@app_blueprint.route('/services')
def services():
    return render_template('flask_/service.html')

@app_blueprint.route('/about')
def about():
    return render_template('flask_/about.html')

@app_blueprint.route('/blog')
def blog():
    users = User.query.all()
    return render_template('flask_/blog.html', users=users)

@app_blueprint.route('/contact')
def contact():
    return render_template('flask_/contact.html')


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