print("Caricamento classe veicolo")

class Veicolo:

    def __init__(self,marca,modello,anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def __str__(self):
        #mostra una tabella allineata a sinistra con intestazioni marca, modello, anno
        return f"| {self.marca:<10} | {self.modello:<10} | {self.anno:<10} |"

def crea_veicolo(marca, modello, anno):
    """Crea e restituisce un'istanza di Veicolo."""
    return Veicolo(marca, modello, anno)
    