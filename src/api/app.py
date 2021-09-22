import logging

from flask import Flask
from flask.cli import with_appcontext

from api.config import config
from data.database import db


def create_app(config_opt: str = "default"):
    app = Flask(__name__)
    app.logger.setLevel(logging.INFO)
    app.config.from_object(config[config_opt])
    config[config_opt].init_app(app)

    db.init_app(app)

    from api.controllers import candidatos_controllers
    app.register_blueprint(candidatos_controllers.bp)

    from api.controllers import contatos_controllers
    app.register_blueprint(contatos_controllers.bp)

    from api.controllers import documentos_controllers
    app.register_blueprint(documentos_controllers.bp)

    @app.cli.command(name='init_db')
    @with_appcontext
    def init_db():
        db.create_all()

    app.cli.add_command(init_db)

    return app
