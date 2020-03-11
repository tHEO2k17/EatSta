from flask import Flask

from app.config.app_config import DevConfig
from app.config.db_config import initialize_db
from app.rest.v1 import status, food, vendor, order


def create_app(config = DevConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    # Database initialization
    initialize_db(app)

    # Blueprints for modularity
    app.register_blueprint(status.blueprint)
    app.register_blueprint(food.blueprint)
    app.register_blueprint(vendor.blueprint)
    app.register_blueprint(order.blueprint)

    return app
