from datetime import datetime
from data.database import db


class Documento(db.Model):
    __tablename__ = 'documentos'
    id = db.Column('id_documento', db.Integer, primary_key=True)
    tipo_documento = db.Column(db.String(50))
    descricao = db.Column(db.String(25))
    pais_emissao = db.Column(db.String(50))
    data_emissao = db.Column(db.DATETIME)
    id_candidato = db.Column(db.Integer, db.ForeignKey('candidatos.id_candidato'))

    def __init__(self, descricao: str, tipo_documento: str, pais_emissao: str, data_emissao: datetime):
        self.descricao = descricao
        self.tipo_documento = tipo_documento
        self.pais_emissao = pais_emissao
        self.data_emissao = data_emissao





