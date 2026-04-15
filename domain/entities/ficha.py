from dataclasses import dataclass

@dataclass(frozen=True)
class Ficha:
    a: int
    b: int

    def es_doble(self) -> bool:
        return self.a == self.b

    def contiene(self, valor: int) -> bool:
        return self.a == valor or self.b == valor

    def voltear(self):
        return Ficha(self.b, self.a)