from werkzeug import Request

from api.response_contents import HttpResponse
from repositories.CandidatoRepository import CandidatoRepository
from util.validation.forms_validation import InsertCandidatoForm
from util.mappers import form_to_candidato
from util.constants.attr_candidato import NOME_USUARIO
from util.constants.error_messages import NAO_MAIS_DISPONIVEL


class CandidatosService:
    def __init__(self, repository: CandidatoRepository):
        self._repository: CandidatoRepository = repository

    def insert_candidato(self, request: Request) -> HttpResponse:
        dados_candidato = InsertCandidatoForm(request.form, csrf_enabled=False)

        if not dados_candidato.validate():
            return HttpResponse.create_error_response(dados_candidato.errors, 400)

        if self._repository.find_by_nome_usuario(request.form['nome_usuario']):
            return HttpResponse.create_error_response({NOME_USUARIO: NAO_MAIS_DISPONIVEL}, 400)

        candidato = form_to_candidato(request.form, hash_password=True)
        self._repository.insert(candidato)

        return HttpResponse.create_success_response("Candidato criado com sucesso", 200)
