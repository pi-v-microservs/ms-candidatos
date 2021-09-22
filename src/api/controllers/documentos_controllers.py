from flask import Blueprint, request

from api.response_contents import HttpResponse
from repositories.DocumentosRepository import DocumentosRepository
from services.DocumentosService import DocumentosService
from util.constants.attr_candidato import ID_CANDIDATO

bp = Blueprint('documentos_controllers', __name__, url_prefix='/documentos')


@bp.route('/get', methods=['GET'])
def get_documento():
    service: DocumentosService = DocumentosService(DocumentosRepository.repository_factory())
    result: HttpResponse = service.get_documento(request)

    return result.to_dict_and_status_code_tuple()


@bp.route('/list', methods=['GET'])
def list_documentos():
    service: DocumentosService = DocumentosService(DocumentosRepository.repository_factory())
    result: HttpResponse = service.list_documentos(request.args.get(ID_CANDIDATO))

    return result.to_dict_and_status_code_tuple()


@bp.route('/create', methods=['POST'])
def create_documento():
    service: DocumentosService = DocumentosService(DocumentosRepository.repository_factory())
    result: HttpResponse = service.insert_documento(request)

    return result.to_dict_and_status_code_tuple()


@bp.route("/update", methods=['PUT'])
def update_documento():
    service: DocumentosService = DocumentosService(DocumentosRepository.repository_factory())
    result: HttpResponse = service.insert_documento(request)

    return result.to_dict_and_status_code_tuple()


@bp.route("/delete", methods=['DELETE'])
def delete_documento():
    service: DocumentosService = DocumentosService(DocumentosRepository.repository_factory())
    result: HttpResponse = service.insert_documento(request)

    return result.to_dict_and_status_code_tuple()
