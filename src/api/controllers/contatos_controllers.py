from flask import Blueprint, request

from api.response_contents import HttpResponse
from repositories.ContatoRepository import ContatoRepository
from services.ContatosService import ContatosService
from util.constants.attr_candidato import ID_CANDIDATO

bp = Blueprint('contatos_controllers', __name__, url_prefix='/contatos')


@bp.route('list', methods=['GET'])
def list_contatos():
    service: ContatosService = ContatosService(ContatoRepository.repository_factory())
    result: HttpResponse = service.list_contatos(request.args.get(ID_CANDIDATO))

    return result.to_dict_and_status_code_tuple()


@bp.route('/get', methods=['GET'])
def get_contato():
    service: ContatosService = ContatosService(ContatoRepository.repository_factory())
    result: HttpResponse = service.get_contato(request)
    return result.to_dict_and_status_code_tuple()


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


@bp.route('delete', methods=['DELETE'])
def delete_contato():
    service: ContatosService = ContatosService(ContatoRepository.repository_factory())
    result: HttpResponse = service.delete_contato(request)

    return result.to_dict_and_status_code_tuple()
