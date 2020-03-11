from mongoengine import StringField

from app.config.db_config import db


class UserModel(db.Document):
    name = StringField(unique=True)