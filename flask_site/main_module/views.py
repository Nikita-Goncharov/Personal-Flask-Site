import os
from datetime import date

from flask import Blueprint, redirect, render_template, url_for, current_app
from werkzeug.utils import secure_filename

from flask_site.extensions import db
from .forms import CommentForm, ContactForm, ServiceForm
from .models import Comment, Service, TechSkill, WorkExperience
from .send_msg_bot import send_msg_bot

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
        name = comment_form.client_name.data
        message = comment_form.message.data
        time = date.today().strftime("%B %d, %Y")
        comment = Comment(name=name, message=message)
        send_msg_bot(name=name, message=message, time=time, type_of_message='comment')
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('app_blue.index'))

    if contact_form.validate_on_submit():
        name = contact_form.name.data
        email = contact_form.email.data
        message = contact_form.message.data
        send_msg_bot(name=name, email=email, message=message, type_of_message='contact')
        return redirect(url_for('app_blue.index'))
    return render_template('main_module/home.html', comment_form=comment_form, contact_form=contact_form,
                           services=services, comments=comments)


@blueprint.route('/resume')
def resume():
    techskills = TechSkill.query.all()
    workexperience = WorkExperience.query.all()
    return render_template('main_module/resume.html', techskills=techskills, workexperience=workexperience)


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


@blueprint.route('/service/<int:id>')
def service(id):
    service_item = Service.query.get(id)
    return render_template('main_module/service_item.html', service=service_item)


@blueprint.route('/contact', methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        name = contact_form.name.data
        email = contact_form.email.data
        message = contact_form.message.data
        send_msg_bot(name=name, email=email, message=message, type_of_message='contact')
        return redirect(url_for('app_blue.index'))
    return render_template('main_module/contact.html', contact_form=contact_form)