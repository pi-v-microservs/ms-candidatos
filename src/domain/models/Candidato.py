from datetime import datetime
from typing import List
from werkzeug.datastructures import ImmutableMultiDict

from data.database import db
from domain.models.Contato import Contato
from domain.models.Documento import Documento
from util.constants.props_candidato import *


class Candidato(db.Model):
    __tablename__ = 'candidatos'
    id = db.Column('id_candidato', db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(50), db.UniqueConstraint())
    senha = db.Column(db.String(250))
    nome_completo = db.Column(db.String(250))
    data_nascimento = db.Column(db.DATETIME)
    nacionalidade = db.Column(db.String(120))
    lingua_nativa = db.Column(db.String(100))
    portugues_fluente = db.Column(db.BOOLEAN)

    contatos: List[Contato] = db.relationship('Contato', backref='candidato')
    documentos: List[Documento] = db.relationship('Documento', backref='documentos')

    def __init__(self, nome_usuario: str,
                 senha: str,
                 nome_completo: str,
                 data_nascimento: datetime,
                 nacionalidade: str,
                 lingua_nativa: str,
                 portugues_fluente: bool):
        self.nome_usuario: str = nome_usuario
        self.senha: str = senha
        self.nome_completo: str = nome_completo
        self.data_nascimento: datetime = data_nascimento
        self.nacionalidade: str = nacionalidade
        self.lingua_nativa: str = lingua_nativa
        self.portugues_fluente: bool = portugues_fluente

    @staticmethod
    def from_form_data(form_data: ImmutableMultiDict):
        return Candidato(nome_usuario=form_data[NOME_USUARIO],
                         senha=form_data[SENHA],
                         nome_completo=form_data[NOME_COMPLETO],
                         data_nascimento=datetime.strptime(form_data[DATA_NASCIMENTO], "%Y-%m-%d"),
                         nacionalidade=form_data[NACIONALIDADE],
                         lingua_nativa=form_data[LINGUA_NATIVA],
                         portugues_fluente={"true": True, "false": False}[form_data[PORTUGUES_FLUENTE].lower()])
