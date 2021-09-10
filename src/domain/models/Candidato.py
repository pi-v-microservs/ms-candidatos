from datetime import datetime
from typing import List
from data.database import db
from domain.models.Contato import Contato
from domain.models.Documento import Documento


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

    def __init__(self, nome_usuario: str, senha: str, nome_completo: str,
                 data_nascimento: datetime, nacionalidade: str, lingua_nativa: str, portugues_fluente: bool):
        self.nome_usuario: str = nome_usuario
        self.senha: str = senha
        self.nome_completo: str = nome_completo
        self.data_nascimento: datetime = data_nascimento
        self.nacionalidade: str = nacionalidade
        self.lingua_nativa: str = lingua_nativa
        self.portugues_fluente: bool = portugues_fluente
