from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Length, NumberRange, Email

from util.constants.attr_candidato import ID_CANDIDATO
from util.constants.attr_contato import *
from util.constants.error_messages import *


class InsertContatoForm(FlaskForm):
    def __init__(self, form_data):
        super().__init__(form_data, csrf_enabled=False)

    descricao = StringField(
        DESCRICAO, validators=[InputRequired(OBRIGATORIO), Length(3, 50, VALORES_ENTRE.format(3, 50))])
    tipo_contato = IntegerField(
        TIPO_CONTATO, validators=[InputRequired(OBRIGATORIO), NumberRange(0, 2, VALORES_ENTRE.format(0, 2))])
    id_candidato = IntegerField(ID_CANDIDATO, validators=[InputRequired(OBRIGATORIO)])


class UpdateContatoForm(FlaskForm):
    def __init__(self, form_data):
        super().__init__(form_data, csrf_enabled=False)

    descricao = StringField(DESCRICAO, validators=[Length(3, 50, VALORES_ENTRE.format(3, 50))])
    tipo_contato = IntegerField(TIPO_CONTATO, validators=[NumberRange(0, 2, VALORES_ENTRE.format(0, 2))])
    id_contato = IntegerField(ID_CONTATO, validators=[InputRequired(OBRIGATORIO)])
