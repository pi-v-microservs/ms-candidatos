from typing import Optional, List

from werkzeug import Request

from api.response_contents import HttpResponse
from domain.models.Candidato import Candidato
from repositories.CandidatoRepository import CandidatoRepository
from util.constants.attr_candidato import NOME_USUARIO, ID_CANDIDATO
from util.constants.entities_names import CANDIDATO
from util.constants.error_messages import NAO_MAIS_DISPONIVEL, NAO_ENCONTRADO
from util.mappers.candidato_mappers import form_to_new_candidato, form_to_existing_candidato
from util.validation.forms.forms_candidato import InsertCandidatoForm, UpdateCandidatoForm, GetCandidatoForm, \
    DeleteCandidatoForm


class CandidatosService:
    def __init__(self, repository: CandidatoRepository):
        self._repository: CandidatoRepository = repository

    def list_candidatos(self) -> HttpResponse:
        candidatos: List[Candidato] = self._repository.get_all()
        candidatos_dicts = [candidato.to_dict() for candidato in candidatos]
        return HttpResponse.create_success_response(candidatos_dicts)

    def get_candidato(self, request: Request) -> HttpResponse:
        dados_filtro = GetCandidatoForm(request.args)

        candidato_output: Optional[Candidato] = None

        if not dados_filtro.validate() and (
                dados_filtro.errors.get(ID_CANDIDATO) and dados_filtro.errors.get(NOME_USUARIO)):
            return HttpResponse.create_error_response(dados_filtro.errors, 403)

        if not dados_filtro.errors.get(ID_CANDIDATO):
            candidato_output = self._repository.find_by(id_candidato=request.args[ID_CANDIDATO])

        if not candidato_output and not dados_filtro.errors.get(NOME_USUARIO):
            candidato_output = self._repository.find_by(nome_usuario=request.args[NOME_USUARIO])

        if not candidato_output:
            return HttpResponse.create_error_response({CANDIDATO: NAO_ENCONTRADO}, 404)

        return HttpResponse.create_success_response(candidato_output.to_dict())

    def insert_candidato(self, request: Request) -> HttpResponse:
        dados_candidato = InsertCandidatoForm(request.form)

        if not dados_candidato.validate():
            return HttpResponse.create_error_response(dados_candidato.errors, 400)

        if self._repository.find_by(nome_usuario=request.form[NOME_USUARIO]):
            return HttpResponse.create_error_response({NOME_USUARIO: NAO_MAIS_DISPONIVEL}, 403)

        candidato = form_to_new_candidato(request.form, hash_password=True)
        self._repository.insert(candidato)

        return HttpResponse.create_success_response({
            'message': 'Candidato criado com sucesso', ID_CANDIDATO: candidato.id_candidato})

    def update_candidato(self, request: Request) -> HttpResponse:
        dados_candidato = UpdateCandidatoForm(request.form)

        if not dados_candidato.validate():
            return HttpResponse.create_error_response(dados_candidato.errors, 400)

        current_candidato = self._repository.find_by(id_candidato=request.form[ID_CANDIDATO])

        if not current_candidato:
            return HttpResponse.create_error_response({NOME_USUARIO: NAO_ENCONTRADO}, 403)

        candidato_update = form_to_existing_candidato(request.form, current_candidato, hash_password=True)

        self._repository.commit()
        return HttpResponse.create_success_response({'message': "Candidato atualizado com sucesso"})

    def delete_candidato(self, request: Request):
        dados_delete_candidato = DeleteCandidatoForm(request.form)

        if not dados_delete_candidato.validate():
            return HttpResponse.create_error_response(dados_delete_candidato.errors, 400)

        candidato_delete = self._repository.find_by(id_candidato=request.form[ID_CANDIDATO])
        self._repository.delete(candidato_delete)

        return HttpResponse.create_success_response({'message': 'Candidato deletado com sucesso'})
