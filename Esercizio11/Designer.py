print("Caricamento classe Designer")

from Dipendente import Dipendente as D

class Designer(D):
    def __init__(self, nome, cognome, email, matricola, stipendio, linguaggio, strumento):
        super().__init__(nome, cognome, email, matricola, stipendio)
        self.linguaggio = linguaggio
        self.strumento = strumento
    
    def __str__(self):
        return (f"\n{'='*30}\n"
                f"Ruolo: Designer\n"
                f"Nome: {self.nome} {self.cognome}\n"
                f"Matricola: {self.matricola}\n"
                f"Email: {self.email}\n"
                f"Stipendio: €{self.stipendio}\n"
                f"Linguaggio: {self.linguaggio}\n"
                f"Strumento: {self.strumento}\n"
                f"{'='*30}")

    