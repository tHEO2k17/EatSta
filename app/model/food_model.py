from app.config.db_config import db
from app.model.status_model import StatusModel
from app.model.vendor_model import VendorModel

# Lib imports
from datetime import datetime


class FoodModel(db.Document):
    name = db.StringField(required=True, unique=True)
    description = db.StringField(required=True, unique=True)
    vendor = db.ReferenceField(VendorModel)
    status = db.ReferenceField(StatusModel)
    date_created = db.DateTimeField(default=datetime.utcnow())
