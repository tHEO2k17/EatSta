from app.config.db_config import db

# Lib imports
from datetime import datetime
import json


class StatusModel(db.Document):
    name = db.StringField(required=True, unique=True)
    description = db.StringField()
    date_created = db.DateTimeField(default=datetime.utcnow())

    def json(self):
        status_dict = {
            "name": self.name,
            "description": self.description,
            "date_created" : self.date_created
        }
        return json.dumps(status_dict)

    meta = {
        "indexes": ["name"],
        "ordering": ["-date_created"]
    }
