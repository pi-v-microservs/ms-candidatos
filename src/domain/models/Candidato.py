import json
from datetime import datetime
from typing import List

from data.database import db
from domain.models.Contato import Contato
from domain.models.Documento import Documento
from util.constants.attr_candidato import ID_CANDIDATO


class Candidato(db.Model):
    __tablename__ = 'candidatos'
    id_candidato = db.Column(ID_CANDIDATO, db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(50), db.UniqueConstraint())
    senha = db.Column(db.String(250))
    nome_completo = db.Column(db.String(250))
    data_nascimento = db.Column(db.DATETIME)
    nacionalidade = db.Column(db.String(120))
    lingua_nativa = db.Column(db.String(100))
    portugues_fluente = db.Column(db.BOOLEAN)

    contatos: List[Contato] = db.relationship('Contato', backref='candidato')
    documentos: List[Documento] = db.relationship('Documento', backref='documentos')

    def __init__(self, id_candidato: int, nome_usuario: str, senha: str, nome_completo: str,
                 data_nascimento: datetime, nacionalidade: str, lingua_nativa: str, portugues_fluente: bool):
        self.id_candidato: int = id_candidato
        self.nome_usuario: str = nome_usuario
        self.senha: str = senha
        self.nome_completo: str = nome_completo
        self.data_nascimento: datetime = data_nascimento
        self.nacionalidade: str = nacionalidade
        self.lingua_nativa: str = lingua_nativa
        self.portugues_fluente: bool = portugues_fluente

    def to_dict(self):
        return {key: val for key, val in self.__dict__.items()
                if not (key == 'senha' or key.startswith('_'))}
