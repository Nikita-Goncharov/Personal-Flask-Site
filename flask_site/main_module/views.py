import json
import os
import subprocess
from datetime import date

from flask import Blueprint, redirect, render_template, url_for, current_app, request
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from flask_site.extensions import db
from .forms import CommentForm, ContactForm, ServiceForm
from .models import Comment, Service, TechSkill, WorkExperience, ShopBasketService
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


@login_required
@blueprint.route('/shop_basket/<int:id>')
def shop_basket(id):
    return render_template("main_module/shop_basket.html", id=id)


@login_required
@blueprint.route("/get_shop_basket_services/<int:id>", methods=["POST"])
def shop_basket_services(id):
    services = []  # {...service}
    user = current_user
    # backet = ShopBasket.query.get(user.basket_id)  # TODO: check if not exists
    basket_services = ShopBasketService.query.filter_by(basket_id=user.basket_id)
    for basket_service in basket_services:
        service = Service.query.filter_by(id=basket_service.service_id).first()
        services.append(service.as_dict())
    return json.dumps({"services": services})


@login_required
@blueprint.route('/add_service_in_basket/<int:service_id>')
def add_service_in_basket(service_id):
    user = current_user
    shop_basket_service = ShopBasketService(basket_id=user.basket_id, service_id=service_id)
    db.session.add(shop_basket_service)
    db.session.commit()
    return redirect(url_for("app_blue.shop_basket", id=user.basket_id))


@blueprint.route('/github_pull_updates', methods=["POST"])
def github_pull_updates():  # TODO: change subprocess.run to something what can be async

    if request.headers.get("X-Hub-Signature") != current_app.config["GITHUB_HOOK_SECRET"]:
        return json.dumps({"message": "Error. Secret keys are not the same", "code": 403})
    try:
        subprocess.run(f"git pull origin develop", shell=True)  # Pull changes from the GitHub repository
    except subprocess.CalledProcessError as ex:
        return json.dumps({"message": f"Error pulling from GitHub: {str(ex)}", "code": 500})

    try:
        # Reload app
        subprocess.run(["touch", "/var/www/develop352_pythonanywhere_com_wsgi.py"], check=True)
    except subprocess.CalledProcessError as ex:
        return json.dumps({"message": f"Error reloading application: {str(ex)}", "code": 500})

    print("CI/CD. Pulling was successful.")
    return json.dumps({"message": "Webhook received and application reloaded successfully", "code": 200})
