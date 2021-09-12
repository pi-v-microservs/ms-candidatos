from typing import Union

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, select
import data.database
from domain.models.Candidato import Candidato
from repositories.BaseRepository import BaseRepository


class CandidatoRepository(BaseRepository):
    def __init__(self, db: SQLAlchemy):
        super().__init__(db)

    @staticmethod
    def repository_factory():
        return CandidatoRepository(data.database.db)

    def find_by(self, **kwargs) -> Union[Candidato, None]:
        return Candidato.query.filter_by(**kwargs).first()

    def get_all(self):
        return Candidato.query.all()

