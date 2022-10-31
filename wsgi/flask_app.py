from flask import Flask


def init_app(config_object) -> Flask:
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_object)
    register_app_blueprints(flask_app)
    return flask_app


def register_app_blueprints(flask_app: Flask) -> None:
    pass
