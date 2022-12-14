from flask import Flask

from wsgi.blueprints.index_blueprint import index_blueprint
from wsgi.blueprints.hero_choosing import choose_blueprint
from wsgi.blueprints.fight_blueprint import fight_blueprint


def init_app(config_object) -> Flask:
    """
    :param config_object: class with configuration settings
    :return: flask app
    """
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_object)
    register_app_blueprints(flask_app)
    return flask_app


def register_app_blueprints(flask_app: Flask) -> None:
    """
    :param flask_app: flask application
    registers all blueprints of flask app
    """
    flask_app.register_blueprint(index_blueprint)
    flask_app.register_blueprint(choose_blueprint)
    flask_app.register_blueprint(fight_blueprint)
