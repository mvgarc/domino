from typing import List
from domain.entities.ficha import Ficha


def es_jugada_valida(ficha: Ficha, extremos: tuple[int, int] | None) -> bool:
    if extremos is None:
        return True

    izq, der = extremos
    return ficha.contiene(izq) or ficha.contiene(der)