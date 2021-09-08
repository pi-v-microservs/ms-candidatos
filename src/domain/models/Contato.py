from domain.enums.TipoContato import TipoContato
from data.database import db


class Contato(db.Model):
    __tablename__ = 'contatos'
    id = db.Column('id_contato', db.Integer, primary_key=True)
    descricao = db.Column(db.String(50))
    complemento = db.Column(db.String(25))
    tipo_contato = db.Column(db.Integer)
    id_candidato = db.Column(db.Integer, db.ForeignKey('candidatos.id_candidato'))

    def __init__(self, descricao: str, complemento: str, tipo_contato: TipoContato):
        self.descricao = descricao
        self.complemento = complemento
        self.tipo_contato = tipo_contato
