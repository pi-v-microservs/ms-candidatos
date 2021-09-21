from typing import Optional

from domain.enums.TipoContato import TipoContato
from data.database import db


class Contato(db.Model):
    __tablename__ = 'contatos'
    id_contato = db.Column('id_contato', db.Integer, primary_key=True)
    descricao = db.Column(db.String(50))
    complemento = db.Column(db.String(25))
    tipo_contato = db.Column(db.Integer)
    id_candidato = db.Column(db.Integer, db.ForeignKey('candidatos.id_candidato'))

    def __init__(self, id_contato: Optional[int], descricao: str,
                 complemento: str, tipo_contato: TipoContato, id_candidato: int):
        self.id_contato: Optional[int] = id_contato
        self.descricao: str = descricao
        self.complemento: str = complemento
        self.tipo_contato: int = tipo_contato.value
        self.id_candidato: int = id_candidato

