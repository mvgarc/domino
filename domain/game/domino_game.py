import random
from domain.entities.ficha import Ficha
from domain.game.state import GameState
from domain.game.rules import es_jugada_valida


class DominoGame:
    def __init__(self, num_jugadores=2):
        self.num_jugadores = num_jugadores
        self.state = GameState()
        self.manos = self._repartir()

    def _crear_fichas(self):
        return [Ficha(i, j) for i in range(7) for j in range(i, 7)]

    def _repartir(self):
        fichas = self._crear_fichas()
        random.shuffle(fichas)
        return [fichas[i*7:(i+1)*7] for i in range(self.num_jugadores)]