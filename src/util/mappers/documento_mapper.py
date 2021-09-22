from datetime import datetime as dt

from werkzeug.datastructures import ImmutableMultiDict

from domain.models.Documento import Documento
from util.constants.attr_candidato import ID_CANDIDATO
from util.constants.attr_documento import *
from util.mappers import use_original_if_src_is_none


def form_to_new_documento(form_data: ImmutableMultiDict):
    return Documento(
        id_documento=None,
        descricao=form_data[DESCRICAO],
        tipo_documento=form_data.get(TIPO_DOCUMENTO),
        pais_emissao=form_data.get(PAIS_EMISSAO),
        data_emissao=dt.strptime(form_data[DATA_EMISSAO], "%Y-%m-%d"),
        id_candidato=form_data.get(ID_CANDIDATO)
    )


def form_to_existing_documento(form_data: ImmutableMultiDict, documento: Documento):
    documento.id_documento = use_original_if_src_is_none(form_data.get(ID_DOCUMENTO), documento.id_documento)
    documento.descricao = use_original_if_src_is_none(form_data.get(DESCRICAO), documento.descricao)
    documento.tipo_documento = use_original_if_src_is_none(form_data.get(TIPO_DOCUMENTO), documento.tipo_documento)
    documento.pais_emissao = use_original_if_src_is_none(form_data.get(PAIS_EMISSAO), documento.pais_emissao)
    documento.data_emissao = use_original_if_src_is_none(form_data.get(DATA_EMISSAO), documento.data_emissao)
    documento.id_candidato = use_original_if_src_is_none(form_data.get(ID_CANDIDATO), documento.id_candidato)
    return documento
