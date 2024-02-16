from datetime import date

from flask_site.extensions import db


class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    service_title = db.Column(db.String(30))
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    filename = db.Column(db.String(100))

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    time = db.Column(db.String(100), default=date.today().strftime("%B %d, %Y"))
    message = db.Column(db.Text)


class TechSkill(db.Model):
    __tablename__ = 'tech_skills'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)


class WorkExperience(db.Model):
    __tablename__ = 'work_experiences'
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(100), unique=True)
    company = db.Column(db.String(100), unique=True)
    period = db.Column(db.String(100))
    text = db.Column(db.Text)


class ShopBasket(db.Model):
    __tablename__ = "shop_baskets"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)


class ShopBasketService(db.Model):
    __tablename__ = "shop_baskets_services"
    id = db.Column(db.Integer, primary_key=True)
    basket_id = db.Column(db.ForeignKey("shop_baskets.id"), nullable=False, )
    service_id = db.Column(db.ForeignKey("services.id"), nullable=False)


class TelegramAdmin(db.Model):
    __tablename__ = "telegram_admins"
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.String(50), unique=True)
    messages_type_access = db.Column(db.String(50))  # "all", "contact", "comments", "order"
