from datetime import datetime
from typing import Optional

from data.database import db


class Documento(db.Model):
    __tablename__ = 'documentos'
    id_documento = db.Column('id_documento', db.Integer, primary_key=True)
    tipo_documento = db.Column(db.String(50))
    descricao = db.Column(db.String(25))
    pais_emissao = db.Column(db.String(50))
    data_emissao = db.Column(db.DATETIME)
    id_candidato = db.Column(db.Integer, db.ForeignKey('candidatos.id_candidato'))

    def __init__(self, id_documento: Optional[int], descricao: str, tipo_documento: str,
                 pais_emissao: str, data_emissao: datetime, id_candidato: int):
        self.id_documento: Optional[int] = id_documento
        self.descricao: str = descricao
        self.tipo_documento: str = tipo_documento
        self.pais_emissao: str = pais_emissao
        self.data_emissao: datetime = data_emissao
        self.id_candidato: int = id_candidato

    def to_dict(self):
        return {key: val for key, val in self.__dict__.items()
                if not key.startswith('_')}
