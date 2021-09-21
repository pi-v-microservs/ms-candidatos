from typing import Optional

from flask_sqlalchemy import SQLAlchemy
import data.database
from domain.models.Candidato import Candidato
from repositories.BaseRepository import BaseRepository


class CandidatoRepository(BaseRepository):
    def __init__(self, db: SQLAlchemy):
        super().__init__(db)

    @staticmethod
    def repository_factory():
        return CandidatoRepository(data.database.db)

    def find_by(self, **kwargs) -> Optional[Candidato]:
        return Candidato.query.filter_by(**kwargs).first()

    def get_all(self):
        return Candidato.query.all()

