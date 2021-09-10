from datetime import datetime
from werkzeug.datastructures import ImmutableMultiDict

from domain.models.Candidato import Candidato
from util.constants.attr_candidato import *
from werkzeug.security import generate_password_hash


def form_to_candidato(form_data: ImmutableMultiDict, hash_password: bool):
    return Candidato(
        nome_usuario=form_data[NOME_USUARIO],
        senha={True: generate_password_hash(form_data[SENHA]), False: form_data[SENHA]}[hash_password],
        nome_completo=form_data[NOME_COMPLETO],
        data_nascimento=datetime.strptime(form_data[DATA_NASCIMENTO], "%Y-%m-%d"),
        nacionalidade=form_data[NACIONALIDADE],
        lingua_nativa=form_data[LINGUA_NATIVA],
        portugues_fluente={"true": True, "false": False}[form_data[PORTUGUES_FLUENTE].lower()]
    )

