from werkzeug import Request

from api.response_contents import HttpResponse
from repositories.CandidatoRepository import CandidatoRepository
from util.validation.forms.forms_candidato import InsertCandidatoForm, UpdateCandidatoForm
from util.mappers import form_to_new_candidato, form_to_existing_candidato
from util.constants.attr_candidato import NOME_USUARIO, ID_CANDIDATO
from util.constants.error_messages import NAO_MAIS_DISPONIVEL, NAO_ENCONTRADO


class CandidatosService:
    def __init__(self, repository: CandidatoRepository):
        self._repository: CandidatoRepository = repository

    def insert_candidato(self, request: Request) -> HttpResponse:
        dados_candidato = InsertCandidatoForm(request.form)

        if not dados_candidato.validate():
            return HttpResponse.create_error_response(dados_candidato.errors, 400)

        if self._repository.find_by(nome_usuario=request.form[NOME_USUARIO]):
            return HttpResponse.create_error_response({NOME_USUARIO: NAO_MAIS_DISPONIVEL}, 403)

        candidato = form_to_new_candidato(request.form, hash_password=True)
        self._repository.insert(candidato)

        return HttpResponse.create_success_response({
            'message': 'Candidato criado com sucesso', ID_CANDIDATO: candidato.id}, 200)

    def update_candidato(self, request: Request) -> HttpResponse:
        dados_candidato = UpdateCandidatoForm(request.form)

        if not dados_candidato.validate():
            return HttpResponse.create_error_response(dados_candidato.errors, 400)

        current_candidato = self._repository.find_by(id_candidato=request.form[ID_CANDIDATO])

        if not current_candidato:
            return HttpResponse.create_error_response({NOME_USUARIO: NAO_ENCONTRADO}, 403)

        candidato_update = form_to_existing_candidato(request.form, current_candidato, hash_password=True)

        self._repository.commit()
        return HttpResponse.create_success_response({'message': "Candidato atualizado com sucesso"}, 200)
