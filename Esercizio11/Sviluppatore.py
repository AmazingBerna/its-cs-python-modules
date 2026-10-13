print("Caricamento classe Sviluppatore")

from Dipendente import Dipendente as D

class Sviluppatore(D):
    def __init__(self, nome, cognome, email, matricola, stipendio, linguaggio, strumento):
        super().__init__(nome, cognome, email, matricola, stipendio)
        self.linguaggio = linguaggio
        self.strumento = strumento
    
    def __str__(self):
        return (f"\n{'='*30}\n"
                f"Ruolo: Sviluppatore\n"
                f"Nome: {self.nome} {self.cognome}\n"
                f"Matricola: {self.matricola}\n"
                f"Email: {self.email}\n"
                f"Stipendio: €{self.stipendio}\n"
                f"Linguaggio: {self.linguaggio}\n"
                f"Strumento: {self.strumento}\n"
                f"{'='*30}")

    