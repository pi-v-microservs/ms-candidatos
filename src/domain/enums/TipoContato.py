import enum


class TipoContato(enum.Enum):
    Telefone = 0
    Celular = 1
    Email = 2


def tipo_contato_from_int(value: int):
    return {0: TipoContato.Telefone, 1: TipoContato.Celular, 2: TipoContato.Email}[value]
