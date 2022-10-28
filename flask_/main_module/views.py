from flask import Blueprint, redirect, render_template, url_for
from .forms import CommentForm, ContactForm
from .models import Comment
from flask_.extensions import db
from .send_msg_bot import send_msg_bot
from datetime import date

blueprint = Blueprint('app_blue', __name__, static_folder='../static',
                        template_folder='../templates', static_url_path='')


@blueprint.route('/', methods=['GET', 'POST'])
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
    return render_template('main_module/home.html', comment_form=comment_form, contact_form=contact_form, comments=comments)


@blueprint.route('/resume')
def resume():
    return render_template('main_module/resume.html')


@blueprint.route('/services')
def services():
    return render_template('main_module/service.html')


@blueprint.route('/about')
def about():
    return render_template('main_module/about.html')


@blueprint.route('/contact', methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        name=contact_form.name.data
        email=contact_form.email.data
        message=contact_form.message.data
        contact = ContactForm(name=name, email=email, message=message)
        send_msg_bot(name=name, email=email, message=message, type_of_message='contact')
        return redirect(url_for('app_blue.index'))
    return render_template('auth_module/contact.html', contact_form=contact_form)
