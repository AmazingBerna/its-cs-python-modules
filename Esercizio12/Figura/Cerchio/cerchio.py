print("Implentazione classe Cerchio")

from Figura.figura import Figura

class Cerchio(Figura):

    def __init__(self, nome, raggio):
        super().__init__(nome)
        self.raggio = raggio

    def __str__(self):
        return (f"\n{'='*30}\n"
                f"Figura: {self.nome}\n"
                f"Raggio: {self.raggio}\n"
                f"Area: {self.area()}\n"
                f"Perimetro: {self.perimetro()}\n"
                f"{'='*30}")
    
    def area(self):
        return 3.14 * (self.raggio * self.raggio)
    
    def perimetro(self):
        return 2 * 3.14 * self.raggio
