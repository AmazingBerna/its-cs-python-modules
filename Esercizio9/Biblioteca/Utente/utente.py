print("Caricamento classe Utente")

class Utente:

    def __init__(self, nome, cognome, eta, email, telefono, indirizzo):

        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.email = email
        self.telefono = telefono
        self.indirizzo = indirizzo
        self.libri_prestati = []

    def __str__(self):
        return f"Nome: {self.nome}\nCognome: {self.cognome}\nEta: {self.eta}\nEmail: {self.email}\nTelefono: {self.telefono}\nIndirizzo: {self.indirizzo}\nLibri prestati: {self.libri_prestati}"