print("Caricamento classe Prestito")

class Prestito:

    def __init__(self, libro, utente, data_prestito, data_restituzione):

        self.libro = libro
        self.utente = utente
        self.data_prestito = data_prestito
        self.data_restituzione = data_restituzione

    def __str__(self):
        return f"Libro: {self.libro}\nUtente: {self.utente}\nData prestito: {self.data_prestito}\nData restituzione: {self.data_restituzione}"