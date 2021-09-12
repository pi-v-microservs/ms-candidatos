from typing import Dict, Tuple, Union, List


class HttpResponse:
    def __init__(self, status: str, content: Dict[str, str], errors: Dict, status_code: int):
        self.status: str = status
        self.content: Dict[str, str] = content
        self.errors: Dict = errors
        self.status_code: int = status_code

    @property
    def has_errors(self):
        return len(self.errors) > 0

    @staticmethod
    def create_success_response(content: Union[Dict[str, str], List[dict]], status_code=200):
        return HttpResponse(status='sucesso', content=content, errors={}, status_code=status_code)

    @staticmethod
    def create_error_response(errors: Dict, status_code: int):
        return HttpResponse(status="erro",
                            content={'message': 'Ocorreram um ou mais erros em sua requisição'},
                            errors=errors,
                            status_code=status_code)

    def to_dict_and_status_code_tuple(self) -> Tuple[Dict, int]:
        return {'status': self.status, 'content': self.content, 'errors': self.errors}, self.status_code

