from flask import Blueprint, redirect, render_template, url_for, current_app
from .forms import CommentForm, ContactForm, ServiceForm
from .models import Comment, Service
from flask_.extensions import db
from .send_msg_bot import send_msg_bot
from datetime import date
from werkzeug.utils import secure_filename
import os

blueprint = Blueprint('app_blue', __name__, static_folder='../static',
                        template_folder='../templates', static_url_path='')


ALLOWED_EXTENSIONS = ('jpeg', 'png', 'jpg')

@blueprint.route('/', methods=['GET', 'POST'])
def index():
    comment_form = CommentForm()
    contact_form = ContactForm()
    services = Service.query.all()
    comments = Comment.query.all()

    if comment_form.validate_on_submit():
        name=comment_form.client_name.data
        message=comment_form.message.data
        time=date.today().strftime("%B %d, %Y")
        comment = Comment(name=name, message=message)
        send_msg_bot(name=name, message=message, time=time, type_of_message='comment')
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('app_blue.index'))

    if contact_form.validate_on_submit():
        name=contact_form.name.data
        email=contact_form.email.data
        message=contact_form.message.data
        send_msg_bot(name=name, email=email, message=message, type_of_message='contact')
        return redirect(url_for('app_blue.index'))
    return render_template('main_module/home.html', comment_form=comment_form, contact_form=contact_form, services=services, comments=comments)


@blueprint.route('/resume')
def resume():
    return render_template('main_module/resume.html')


def allowed_filename(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@blueprint.route('/services', methods=['GET', 'POST'])
def services():
    service_form = ServiceForm()
    services = Service.query.all()
    if service_form.validate_on_submit():
        title = service_form.title.data
        description = service_form.description.data
        file = service_form.logo.data

        if file and allowed_filename(file.filename):
            filename = secure_filename(file.filename)

            if not os.path.exists(current_app.config['UPLOAD_FOLDER']):
                os.mkdir(current_app.config['UPLOAD_FOLDER'])
            img_link = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(img_link)

        service = Service(service_title=title, description=description, filename=filename)
        db.session.add(service)
        db.session.commit() 
        return redirect(url_for('app_blue.services'))
    return render_template('main_module/service.html', service_form=service_form, services=services)


@blueprint.route('/contact', methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        name=contact_form.name.data
        email=contact_form.email.data
        message=contact_form.message.data
        send_msg_bot(name=name, email=email, message=message, type_of_message='contact')
        return redirect(url_for('app_blue.index'))
    return render_template('main_module/contact.html', contact_form=contact_form)
