from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField
from wtforms.validators import InputRequired, Length
from util.constants.error_messages import *
from .custom_validators import YearSpan


class InsertCandidatoForm(FlaskForm):
    nome_usuario = StringField(
        'nome_usuario', validators=[InputRequired(OBRIGATORIO), Length(3, 50, VALORES_ENTRE.format(3, 50))])
    senha = StringField('senha', validators=[InputRequired(OBRIGATORIO), Length(8, 250, VALORES_ENTRE.format(8, 250))])
    nome_completo = StringField('nome_completo', validators=[InputRequired(OBRIGATORIO),
                                                             Length(1, 250, VALORES_ENTRE.format(1, 250))])
    data_nascimento = DateField('data_nascimento', validators=[YearSpan(1989, datetime.now().year - 14)])
    nacionalidade = StringField('nacionalidade', validators=[InputRequired(OBRIGATORIO),
                                                             Length(2, 120, VALORES_ENTRE.format(2, 120))])
    lingua_nativa = StringField('lingua_nativa', validators=[InputRequired(OBRIGATORIO),
                                                             Length(2, 100, VALORES_ENTRE.format(2, 100))])
    portugues_fluente = BooleanField('portugues_fluente', validators=[InputRequired(OBRIGATORIO)])




