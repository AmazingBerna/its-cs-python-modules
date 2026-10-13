print("Implentazione classe triangolo")

from Figura.figura import Figura

class Triangolo(Figura):

    def __init__(self, nome, base, altezza):
        super().__init__(nome)
        self.base = base
        self.altezza = altezza

    def __str__(self):
        return (f"\n{'='*30}\n"
                f"Figura: {self.nome}\n"
                f"Base: {self.base}\n"
                f"Altezza: {self.altezza}\n"
                f"Area: {self.area()}\n"
                f"{'='*30}")
    
    def area(self):
        return (self.base * self.altezza) / 2