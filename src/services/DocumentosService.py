from typing import List

from werkzeug import Request

from api.response_contents import HttpResponse
from domain.models.Contato import Contato
from repositories.DocumentosRepository import DocumentosRepository
from util.constants.attr_documento import ID_DOCUMENTO
from util.constants.entities_names import DOCUMENTO
from util.constants.error_messages import NAO_ENCONTRADO
from util.mappers.documento_mapper import form_to_new_documento


class DocumentosService:
    def __init__(self, repository: DocumentosRepository):
        self._repository: DocumentosRepository = repository

    def get_documento(self, request: Request):
        documento = self._repository.find_documento_by_id(request.args)
        return HttpResponse.create_success_response(documento.to_dict())

    def list_documentos(self, id_candidato: int):
        documentos: List[Contato] = []

        if id_candidato:
            documentos = self._repository.get_documentos_candidato(id_candidato)
        else:
            documentos = self._repository.get_all()

        documentos_dicts = [documento.to_dict() for documento in documentos]
        return HttpResponse.create_success_response(documentos_dicts)

    def insert_documento(self, request: Request) -> HttpResponse:
        self._repository.insert(form_to_new_documento(request.form))
        return HttpResponse.create_success_response(
            {'message': 'Documento criado com sucesso', ID_DOCUMENTO: request.form[ID_DOCUMENTO]})

    def update_documento(self, request: Request) -> HttpResponse:
        documento_existente = self._repository.find_documento_by_id(request.form)

        if not documento_existente:
            return HttpResponse.create_error_response({DOCUMENTO: NAO_ENCONTRADO}, 403)

        self._repository.commit()
        return HttpResponse.create_success_response({'message': 'Documento atualizado com sucesso'})

    def delete_contato(self, request: Request):
        documento_delete = self._repository.find_documento_by_id(request.form)
        self._repository.delete(documento_delete)

        return HttpResponse.create_success_response({'message': 'Documento deletado com sucesso'})
