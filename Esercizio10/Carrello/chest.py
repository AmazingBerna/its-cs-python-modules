
class Chest():
    
    def __init__(self, lista_prodotti):
        self.lista_prodotti = lista_prodotti

    def add_product(self, prodotto):
        self.lista_prodotti.append(prodotto)

    def remove_product(self, nome):
        for prodotto in self.lista_prodotti:
            if prodotto.nome == nome:
                self.lista_prodotti.remove(prodotto)
                break

    def empty_chest(self):
        self.lista_prodotti = []

    def show_chest(self):
        print("IL TUO CARRELLO")
        print("-" * 50)
        for prodotto in self.lista_prodotti:
            print(f"| Nome: {prodotto.nome} | Prezzo: {prodotto.prezzo} | Quantità: {prodotto.quantita} |")
        print("-" * 50)

    def calculate_total(self):
        totale = 0
        for prodotto in self.lista_prodotti:
            totale += prodotto.prezzo * prodotto.quantita
        return totale