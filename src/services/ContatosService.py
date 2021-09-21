from typing import Optional

from werkzeug import Request

from api.response_contents import HttpResponse
from domain.models.Contato import Contato
from repositories.ContatoRepository import ContatoRepository
from util.constants.attr_contato import ID_CONTATO, DESCRICAO
from util.constants.error_messages import CONTATO_JA_EXISTE, CONTATO_NAO_EXISTE
from util.mappers.contato_mappers import form_to_new_contato, form_to_existing_contato
from util.validation.forms.forms_contato import InsertContatoForm, UpdateContatoForm
from util.validation.validation_functions import validate_conteudo_contato


class ContatosService:
    def __init__(self, repository: ContatoRepository):
        self._repository: ContatoRepository = repository

    def insert_contato(self, request: Request) -> HttpResponse:
        dados_contato = InsertContatoForm(request.form)

        if not dados_contato.validate():
            return HttpResponse.create_error_response(dados_contato.errors, 400)

        if self._repository.find_contato(request.form):
            return HttpResponse.create_error_response({DESCRICAO: CONTATO_JA_EXISTE}, 403)

        contato = form_to_new_contato(request.form)

        erros_validacao_conteudo = validate_conteudo_contato(contato)

        if erros_validacao_conteudo:
            return HttpResponse.create_error_response(erros_validacao_conteudo, 403)

        self._repository.insert(contato)

        return HttpResponse.create_success_response({
            'message': 'Contato criado com sucesso', ID_CONTATO: contato.id_contato}, 200)

    def update_contato(self, request: Request) -> HttpResponse:
        dados_contato = UpdateContatoForm(request.form)

        if not dados_contato.validate():
            return HttpResponse.create_error_response(dados_contato.errors, 400)

        contato_existente: Optional[Contato] = self._repository.find_contato_by_id(request.form)

        if not contato_existente:
            return HttpResponse.create_error_response({DESCRICAO: CONTATO_NAO_EXISTE}, 403)

        contato = form_to_existing_contato(request.form, contato_existente)

        erros_validacao_conteudo = validate_conteudo_contato(contato)

        if erros_validacao_conteudo:
            return HttpResponse.create_error_response(erros_validacao_conteudo, 403)

        self._repository.commit()

        return HttpResponse.create_success_response({
            'message': 'Contato atualizado com sucesso', ID_CONTATO: contato.id_contato}, 200)