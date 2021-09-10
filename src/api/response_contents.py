from typing import Dict, Tuple


class HttpResponse:
    def __init__(self, status: str, message: str, errors: Dict, status_code: int):
        self.status: str = status
        self.message: str = message
        self.errors: Dict = errors
        self.status_code: int = status_code

    @property
    def has_errors(self):
        return len(self.errors) > 0

    @staticmethod
    def create_success_response(message: str, status_code=200):
        return HttpResponse(status="sucesso", message=message, errors={}, status_code=status_code)

    @staticmethod
    def create_error_response(errors: Dict, status_code: int):
        return HttpResponse(status="erro",
                            message="Ocorreram um ou mais erros em sua requisição",
                            errors=errors,
                            status_code=status_code)

    def to_dict_and_status_code_tuple(self) -> Tuple[Dict, int]:
        return {'status': self.status, 'message': self.message, 'errors': self.errors}, self.status_code

