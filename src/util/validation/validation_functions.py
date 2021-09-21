from typing import Dict, List

from domain.models.Contato import Contato
import re

from util.constants.attr_contato import DESCRICAO, COMPLEMENTO
from util.constants.error_messages import APENAS_DIGITOS, EMAIL_INVALIDO
from wtforms.validators import email


def validate_conteudo_contato(contato: Contato):
    return {0: validate_telefone_or_celular,
            1: validate_telefone_or_celular,
            2: validate_email}[int(contato.tipo_contato)](contato)


def validate_telefone_or_celular(contato: Contato):
    errors: Dict[str, List[str]] = {}

    if not re.match('^[0-9]*$', contato.descricao):
        errors[DESCRICAO] = [APENAS_DIGITOS]

    if not re.match('^[0-9]*$', contato.complemento):
        errors[COMPLEMENTO] = [APENAS_DIGITOS]

    return errors


def validate_email(contato: Contato):
    errors: Dict[str, List[str]] = {}

    if not re.match(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", contato.descricao):
        errors[DESCRICAO] = [EMAIL_INVALIDO]

    return errors
