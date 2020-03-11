from app.config.db_config import db
from app.model.status_model import StatusModel

# Lib imports
from datetime import datetime


class VendorModel(db.Document):
    name = db.StringField(required=True, unique=True)
    location = db.StringField(required=True, unique=True)
    contact = db.StringField(required=True, unique=True)
    start_date = db.DateTimeField(default=datetime.utcnow())
    end_date = db.DateTimeField()
    status = db.ReferenceField(StatusModel)
    date_created = db.DateTimeField(default=datetime.utcnow())
