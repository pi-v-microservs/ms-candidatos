from typing import Optional

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from werkzeug.datastructures import ImmutableMultiDict, MultiDict

import data.database
from domain.models.Contato import Contato
from domain.models.Documento import Documento
from repositories.BaseRepository import BaseRepository
from util.constants.attr_candidato import ID_CANDIDATO
from util.constants.attr_contato import DESCRICAO, TIPO_CONTATO
from util.constants.attr_documento import ID_DOCUMENTO


class DocumentosRepository(BaseRepository):
    def __init__(self, db: SQLAlchemy):
        super().__init__(db)

    @staticmethod
    def repository_factory():
        return DocumentosRepository(data.database.db)

    def find_documento(self, form_data: ImmutableMultiDict) -> Optional[Contato]:
        return Documento.query.filter(
            and_(
                Documento.id_candidato == form_data[ID_CANDIDATO],
                Documento.descricao == form_data[DESCRICAO],
                Documento.tipo_documento == int(form_data[TIPO_CONTATO]))).first()

    def find_documento_by_id(self, form_data: MultiDict) -> Optional[Contato]:
        return Documento.query.filter_by(id_documento=form_data[ID_DOCUMENTO]).first()

    def get_all(self):
        return Documento.query.all()

    def get_documentos_candidato(self, id_candidato: int):
        return Documento.query.filter_by(id_candidato=id_candidato).all()
