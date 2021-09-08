from werkzeug import Request
from werkzeug.datastructures import ImmutableMultiDict

from domain.models.Candidato import Candidato
from util.constants import props_candidato
from repositories.CandidatosRepository import BaseRepository
from util.validation.ValidationResult import ValidationResultBuilder, ValidationResult
from util.validation.validation_functions import *


class CandidatosService:
    def __init__(self, repository: BaseRepository):
        self._repository = repository
        self._validator: CandidatoValidator = CandidatoValidator()

    def insert_candidato(self, request: Request):
        validation_result: ValidationResult = self._validator.validate_insert_candidato(request.form)

        if not validation_result.has_errors():
            candidato = Candidato.from_form_data(request.form)
            self._repository.insert(candidato)

        return validation_result


class CandidatoValidator:
    def __init__(self):
        self._model_attributes = {x.lower() for x in vars(props_candidato).keys() if "_" not in x[0]}
        self._result_builder: ValidationResultBuilder = ValidationResultBuilder.new()
        self._validation_rules = {
            props_candidato.NOME_COMPLETO: [lambda val: has_at_least(2, val), is_required],
            props_candidato.SENHA: [lambda val: has_at_least(8, val), is_required]}

    def validate_insert_candidato(self, form_data: ImmutableMultiDict) -> ValidationResult:
        self._result_builder.use_missing_attributes_check(form_data, self._model_attributes)
        self._result_builder.use_field_validation_rules(form_data, self._validation_rules)
        return self._result_builder.build()
