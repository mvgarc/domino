from typing import List, Optional
from domain.entities.ficha import Ficha


class GameState:
    def __init__(self):
        self.mesa: List[Ficha] = []
        self.turno: int = 0
        self.pases_consecutivos: int = 0

    def extremos(self) -> Optional[tuple[int, int]]:
        if not self.mesa:
            return None
        return self.mesa[0].a, self.mesa[-1].b