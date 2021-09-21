from typing import Optional

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from werkzeug.datastructures import ImmutableMultiDict

import data.database
from domain.models.Contato import Contato
from repositories.BaseRepository import BaseRepository
from util.constants.attr_candidato import ID_CANDIDATO
from util.constants.attr_contato import DESCRICAO, TIPO_CONTATO, ID_CONTATO


class ContatoRepository(BaseRepository):
    def __init__(self, db: SQLAlchemy):
        super().__init__(db)

    @staticmethod
    def repository_factory():
        return ContatoRepository(data.database.db)

    def find_contato(self, form_data: ImmutableMultiDict) -> Optional[Contato]:
        return Contato.query.filter(
            and_(
                Contato.id_candidato == form_data[ID_CANDIDATO],
                Contato.descricao == form_data[DESCRICAO],
                Contato.tipo_contato == int(form_data[TIPO_CONTATO]))).first()

    def find_contato_by_id(self, form_data: ImmutableMultiDict) -> Optional[Contato]:
        return Contato.query.filter_by(id_contato=form_data[ID_CONTATO]).first()

    def get_all(self):
        return Contato.query.all()

    def get_contatos_candidato(self, id_candidato: int):
        return Contato.query.filter_by(id_candidato=id_candidato).all()
