import logging
from flask import Flask
from config import config
from data.database import db


def create_app(config_opt: str = "default"):
    app = Flask(__name__)
    app.logger.setLevel(logging.INFO)
    app.config.from_object(config[config_opt])
    config[config_opt].init_app(app)

    from domain.models import Candidato, Contato, Documento
    db.init_app(app)

    from controllers import candidatos_controllers
    app.register_blueprint(candidatos_controllers.bp)

    return app