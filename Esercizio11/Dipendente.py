print("Caricamento classe Dipendente")

class Dipendente:
    def __init__(self, nome, cognome, email, matricola, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.matricola = matricola
        self.stipendio = stipendio
    
    def __str__(self):
        return (f"\n{'='*30}\n"
                f"Ruolo: Dipendente\n"
                f"Nome: {self.nome} {self.cognome}\n"
                f"Matricola: {self.matricola}\n"
                f"Email: {self.email}\n"
                f"Stipendio: €{self.stipendio}\n"
                f"{'='*30}")
