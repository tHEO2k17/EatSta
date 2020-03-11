from app.config.db_config import db
from app.model.food_model import FoodModel
from app.model.status_model import StatusModel
from app.model.user_model import UserModel

# Lib imports
from datetime import datetime


class OrderModel(db.Document):
    user = db.ReferenceField(UserModel)
    food = db.ReferenceField(FoodModel)
    status = db.ReferenceField(StatusModel)
    date_created = db.DateTimeField(default=datetime.utcnow())
