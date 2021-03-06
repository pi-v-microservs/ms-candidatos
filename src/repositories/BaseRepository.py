from flask_sqlalchemy import SQLAlchemy, Model

import data.database


class BaseRepository:
    def __init__(self, db: SQLAlchemy):
        self._db = db

    @staticmethod
    def repository_factory():
        return BaseRepository(data.database.db)

    def insert(self, model: Model):
        self._db.session.add(model)
        self._db.session.commit()

    def delete(self, model: Model):
        self._db.session.delete(model)
        self._db.session.commit()

    def commit(self):
        self._db.session.commit()
