from collections import Callable
from datetime import datetime as dt
from werkzeug.datastructures import ImmutableMultiDict

from domain.models.Candidato import Candidato
from util.constants.attr_candidato import *
from werkzeug.security import generate_password_hash


def form_to_new_candidato(form_data: ImmutableMultiDict, hash_password: bool):
    return Candidato(
        nome_usuario=form_data[NOME_USUARIO],
        senha={True: generate_password_hash(form_data[SENHA]), False: form_data[SENHA]}[hash_password],
        nome_completo=form_data[NOME_COMPLETO],
        data_nascimento=dt.strptime(form_data[DATA_NASCIMENTO], "%Y-%m-%d"),
        nacionalidade=form_data[NACIONALIDADE],
        lingua_nativa=form_data[LINGUA_NATIVA],
        portugues_fluente={"true": True, "false": False}[form_data[PORTUGUES_FLUENTE].lower()]
    )


def form_to_existing_candidato(form_data: ImmutableMultiDict, candidato: Candidato, hash_password: bool):
    candidato.nome_usuario = use_original_if_src_is_none(form_data.get(NOME_USUARIO), candidato.nome_usuario)
    candidato.senha = use_original_if_src_is_none(
            form_data.get(SENHA), candidato.senha, mutate={True: generate_password_hash, False: None}[hash_password])
    candidato.nome_completo = use_original_if_src_is_none(form_data.get(NOME_COMPLETO), candidato.nome_completo)
    candidato.data_nascimento = use_original_if_src_is_none(
            form_data.get(DATA_NASCIMENTO), candidato.data_nascimento, mutate=lambda val: dt.strptime(val, "%Y-%m-%d"))
    candidato.nacionalidade = use_original_if_src_is_none(form_data.get(NACIONALIDADE), candidato.nacionalidade)
    candidato.lingua_nativa = use_original_if_src_is_none(form_data.get(LINGUA_NATIVA), candidato.lingua_nativa)
    candidato.portugues_fluente = use_original_if_src_is_none(
        form_data.get(PORTUGUES_FLUENTE),
        candidato.portugues_fluente,
        mutate=lambda val: {"true": True, "false": False}[val.lower()])

    return candidato


def use_original_if_src_is_none(source, original, mutate: Callable = None):
    if source is None:
        return original

    if mutate is None:
        return source
    else:
        return mutate(source)


