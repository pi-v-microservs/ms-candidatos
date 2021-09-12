from flask import Blueprint, request

from api.response_contents import HttpResponse
from repositories.CandidatoRepository import CandidatoRepository
from services.CandidatosService import CandidatosService

bp = Blueprint('candidatos_controllers', __name__, url_prefix="/candidatos")


@bp.route("/")
def index():
    return "hello!"


@bp.route("/create", methods=['POST'])
def candidatos_create():
    service: CandidatosService = CandidatosService(CandidatoRepository.repository_factory())
    result: HttpResponse = service.insert_candidato(request)

    return result.to_dict_and_status_code_tuple()


@bp.route("update", methods=['POST'])
def candidatos_update():
    service: CandidatosService = CandidatosService(CandidatoRepository.repository_factory())
    result: HttpResponse = service.update_candidato(request)

    return result.to_dict_and_status_code_tuple()
