from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Length

from util.constants.attr_candidato import *
from util.constants.error_messages import *
from util.validation.custom_validators import YearSpan


class GetCandidatoForm(FlaskForm):
    def __init__(self, form_data):
        super().__init__(form_data, csrf_enabled=False)
    id_candidato = IntegerField(ID_CANDIDATO, validators=[
        InputRequired(message=NECESSARIO_INFORMAR_X_OU_Y.format(x=ID_CANDIDATO, y=NOME_USUARIO))])
    nome_usuario = StringField(NOME_USUARIO, validators=[
        InputRequired(message=NECESSARIO_INFORMAR_X_OU_Y.format(x=ID_CANDIDATO, y=NOME_USUARIO))])


class InsertCandidatoForm(FlaskForm):
    def __init__(self, form_data):
        super().__init__(form_data, csrf_enabled=False)

    nome_usuario = StringField(
        NOME_USUARIO, validators=[InputRequired(OBRIGATORIO), Length(3, 50, VALORES_ENTRE.format(3, 50))])
    senha = StringField(SENHA, validators=[InputRequired(OBRIGATORIO), Length(8, 250, VALORES_ENTRE.format(8, 250))])
    nome_completo = StringField(NOME_COMPLETO, validators=[InputRequired(OBRIGATORIO),
                                                           Length(1, 250, VALORES_ENTRE.format(1, 250))])
    data_nascimento = DateField(DATA_NASCIMENTO, validators=[YearSpan(1989, datetime.now().year - 14)])
    nacionalidade = StringField(NACIONALIDADE, validators=[InputRequired(OBRIGATORIO),
                                                           Length(2, 120, VALORES_ENTRE.format(2, 120))])
    lingua_nativa = StringField(LINGUA_NATIVA, validators=[InputRequired(OBRIGATORIO),
                                                           Length(2, 100, VALORES_ENTRE.format(2, 100))])
    portugues_fluente = BooleanField(PORTUGUES_FLUENTE, validators=[InputRequired(OBRIGATORIO)])


class UpdateCandidatoForm(FlaskForm):
    def __init__(self, form_data):
        super().__init__(form_data, csrf_enabled=False)
    id_candidato = IntegerField(ID_CANDIDATO, validators=[InputRequired(message=OBRIGATORIO)])
    nome_usuario = StringField(NOME_USUARIO, validators=[Length(3, 50, VALORES_ENTRE.format(3, 50))])
    senha = StringField(SENHA, validators=[Length(8, 250, VALORES_ENTRE.format(8, 250))])
    nome_completo = StringField(NOME_COMPLETO, validators=[Length(1, 250, VALORES_ENTRE.format(1, 250))])
    data_nascimento = DateField(DATA_NASCIMENTO, validators=[YearSpan(1989, datetime.now().year - 14)])
    nacionalidade = StringField(NACIONALIDADE, validators=[Length(2, 120, VALORES_ENTRE.format(2, 120))])
    lingua_nativa = StringField(LINGUA_NATIVA, validators=[Length(2, 100, VALORES_ENTRE.format(2, 100))])
    portugues_fluente = BooleanField(PORTUGUES_FLUENTE, validators=[InputRequired(OBRIGATORIO)])
