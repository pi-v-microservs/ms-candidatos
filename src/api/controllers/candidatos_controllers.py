from flask import Blueprint, request
from repositories.CandidatosRepository import BaseRepository
from services.CandidatosService import CandidatosService
from util.validation.ValidationResult import ValidationResult

bp = Blueprint('candidatos_controllers', __name__)


@bp.route("/")
def index():
    return "hello!"


@bp.route("/create", methods=['POST'])
def candidatos_create():
    service: CandidatosService = CandidatosService(BaseRepository.repository_factory())
    result: ValidationResult = service.insert_candidato(request)

    if result.has_errors():
        return {"errors": result.errors}, 400

    return "", 200



