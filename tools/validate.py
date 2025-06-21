from typing import get_type_hints, Union
from collections import OrderedDict
from config import MovieEntry


def validar_e_ordenar(d: MovieEntry) -> MovieEntry:
    hints = get_type_hints(MovieEntry)

    # Verifica obrigatórios
    for campo in MovieEntry.__required_keys__:
        if campo not in d:
            raise ValueError(f"Campo obrigatório '{campo}' ausente")

    # Validação de tipos para todos os campos presentes
    for field, typ in hints.items():
        if field in d:
            val = d[field]
            # Trata Optional (que é Union[..., NoneType])
            if getattr(typ, "__origin__", None) is Union:
                tipos_validos = [t for t in typ.__args__ if t is not type(None)]
                if not any(isinstance(val, t) for t in tipos_validos):
                    raise TypeError(
                        f"Campo '{field}' em '{d.get('Title', '')}' deve ser um dos tipos {tipos_validos}, "
                        f"mas recebeu {type(val)}"
                    )
            else:
                if not isinstance(val, typ):
                    raise TypeError(
                        f"Campo '{field}' em '{d.get('Title', '')}' deve ser {typ}, mas recebeu {type(val)}"
                    )

    # Ordena só os campos que existem no dicionário
    ordered = OrderedDict()
    for field in hints.keys():
        if field in d:
            ordered[field] = d[field]

    return ordered  # type: ignore
