from werkzeug.datastructures import ImmutableMultiDict

from domain.enums.TipoContato import tipo_contato_from_int
from domain.models.Contato import Contato
from util.constants.attr_candidato import ID_CANDIDATO
from util.constants.attr_contato import DESCRICAO, COMPLEMENTO, TIPO_CONTATO
from util.mappers import use_original_if_src_is_none


def form_to_new_contato(form_data: ImmutableMultiDict):
    return Contato(
        id_contato=None,
        descricao=form_data[DESCRICAO],
        complemento=form_data.get(DESCRICAO),
        tipo_contato=tipo_contato_from_int(int(form_data[TIPO_CONTATO])),
        id_candidato=int(form_data[ID_CANDIDATO])
    )


def form_to_existing_contato(form_data: ImmutableMultiDict, contato: Contato):
    contato.complemento = use_original_if_src_is_none(form_data.get(COMPLEMENTO), contato.complemento)
    contato.descricao = use_original_if_src_is_none(form_data.get(DESCRICAO), contato.descricao)
    contato.tipo_contato = use_original_if_src_is_none(form_data.get(TIPO_CONTATO), contato.tipo_contato)
    return contato

