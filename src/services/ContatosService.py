from typing import Optional, List

from werkzeug import Request

from api.response_contents import HttpResponse
from domain.models.Contato import Contato
from repositories.ContatoRepository import ContatoRepository
from util.constants.attr_contato import ID_CONTATO, DESCRICAO
from util.constants.entities_names import CONTATO
from util.constants.error_messages import CONTATO_JA_EXISTE, NAO_ENCONTRADO
from util.mappers.contato_mappers import form_to_new_contato, form_to_existing_contato
from util.validation.forms.forms_contato import InsertContatoForm, UpdateContatoForm, GetContatoPorIdForm
from util.validation.validation_functions import validate_conteudo_contato


class ContatosService:
    def __init__(self, repository: ContatoRepository):
        self._repository: ContatoRepository = repository

    def get_contato(self, request: Request):
        dados_contato = GetContatoPorIdForm(request.args)

        if not dados_contato.validate():
            return HttpResponse.create_error_response(dados_contato.errors, 400)

        contato = self._repository.find_contato_by_id(request.args)

        return HttpResponse.create_success_response(contato.to_dict(), 200)

    def list_contatos(self, id_candidato: int):
        contatos: List[Contato] = []

        if id_candidato:
            contatos = self._repository.get_contatos_candidato(id_candidato)
        else:
            contatos = self._repository.get_all()

        contatos_dicts = [contato.to_dict() for contato in contatos]
        return HttpResponse.create_success_response(contatos_dicts)

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
            'message': 'Contato criado com sucesso', ID_CONTATO: contato.id_contato})

    def update_contato(self, request: Request) -> HttpResponse:
        dados_contato = UpdateContatoForm(request.form)

        if not dados_contato.validate():
            return HttpResponse.create_error_response(dados_contato.errors, 400)

        contato_existente: Optional[Contato] = self._repository.find_contato_by_id(request.form)

        if not contato_existente:
            return HttpResponse.create_error_response({CONTATO: NAO_ENCONTRADO}, 403)

        contato = form_to_existing_contato(request.form, contato_existente)

        erros_validacao_conteudo = validate_conteudo_contato(contato)

        if erros_validacao_conteudo:
            return HttpResponse.create_error_response(erros_validacao_conteudo, 403)

        self._repository.commit()

        return HttpResponse.create_success_response({
            'message': 'Contato atualizado com sucesso', ID_CONTATO: contato.id_contato}, 200)

    def delete_contato(self, request: Request):
        dados_delete_contato = GetContatoPorIdForm(request.form)

        if not dados_delete_contato.validate():
            return HttpResponse.create_error_response(dados_delete_contato.errors, 400)

        contato_delete = self._repository.find_contato_by_id(request.form)
        self._repository.delete(contato_delete)

        return HttpResponse.create_success_response({'message': 'Contato deletado com sucesso'})