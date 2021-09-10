from flask import Blueprint, request

from api.response_contents import HttpResponse
from repositories.CandidatoRepository import CandidatoRepository
from services.CandidatosService import CandidatosService

bp = Blueprint('candidatos_controllers', __name__)


@bp.route("/")
def index():
    return "hello!"


@bp.route("/create", methods=['POST'])
def candidatos_create():
    service: CandidatosService = CandidatosService(CandidatoRepository.repository_factory())
    result: HttpResponse = service.insert_candidato(request)

    if result.has_errors:
        return result.to_dict_and_status_code_tuple()

    return result.to_dict_and_status_code_tuple()
