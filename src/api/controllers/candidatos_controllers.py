from flask import Blueprint, request

from api.response_contents import HttpResponse
from repositories.CandidatoRepository import CandidatoRepository
from services.CandidatosService import CandidatosService

bp = Blueprint('candidatos_controllers', __name__, url_prefix='/candidatos')


@bp.route('/list', methods=['GET'])
def list_candidatos():
    service: CandidatosService = CandidatosService(CandidatoRepository.repository_factory())
    result: HttpResponse = service.list_candidatos()

    return result.to_dict_and_status_code_tuple()


@bp.route('/get', methods=['GET'])
def get_candidato():
    service: CandidatosService = CandidatosService(CandidatoRepository.repository_factory())
    result: HttpResponse = service.get_candidato(request)
    return result.to_dict_and_status_code_tuple()


@bp.route('/create', methods=['POST'])
def create_candidato():
    service: CandidatosService = CandidatosService(CandidatoRepository.repository_factory())
    result: HttpResponse = service.insert_candidato(request)

    return result.to_dict_and_status_code_tuple()


@bp.route('/update', methods=['PUT'])
def update_candidato():
    service: CandidatosService = CandidatosService(CandidatoRepository.repository_factory())
    result: HttpResponse = service.update_candidato(request)

    return result.to_dict_and_status_code_tuple()


@bp.route('/delete', methods=['DELETE'])
def delete_candidato():
    service: CandidatosService = CandidatosService(CandidatoRepository.repository_factory())
    result: HttpResponse = service.delete_candidato(request)

    return result.to_dict_and_status_code_tuple()
