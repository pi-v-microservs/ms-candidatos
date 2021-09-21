from flask import Blueprint, request

from api.response_contents import HttpResponse
from repositories.CandidatoRepository import CandidatoRepository
from repositories.ContatoRepository import ContatoRepository
from services.CandidatosService import CandidatosService
from services.ContatosService import ContatosService

bp = Blueprint('contatos_controllers', __name__, url_prefix='/contatos')

#
# @bp.route('list', methods=['GET'])
# def list_contatos():
#     service: CandidatosService = CandidatosService(CandidatoRepository.repository_factory())
#     result: HttpResponse = service.list_candidatos(request)
#
#     return result.to_dict_and_status_code_tuple()


# @bp.route('/get', methods=['GET'])
# def get_candidato():
#     service: CandidatosService = CandidatosService(CandidatoRepository.repository_factory())
#     result: HttpResponse = service.get_candidato(request)
#     return result.to_dict_and_status_code_tuple()


@bp.route('/create', methods=['POST'])
def create_candidato():
    service: ContatosService = ContatosService(ContatoRepository.repository_factory())
    result: HttpResponse = service.insert_contato(request)

    return result.to_dict_and_status_code_tuple()


@bp.route('update', methods=['PUT'])
def update_contato():
    service: ContatosService = ContatosService(ContatoRepository.repository_factory())
    result: HttpResponse = service.update_contato(request)

    return result.to_dict_and_status_code_tuple()
