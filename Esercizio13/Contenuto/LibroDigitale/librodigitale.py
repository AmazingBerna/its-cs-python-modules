print("Caricamento classe Libro Digitale")

from Contenuto.contenuto import Contenuto

class LibroDigitale(Contenuto):

    def __init__(self,titolo, autore, durata, numero_pagine, codice_attivazione):
        super().__init__(titolo, autore, durata)
        self.numero_pagine = numero_pagine
        self.codice_attivazione = codice_attivazione

    def __str__(self):
        return (f"\n{'='*30}\n"
                f"Titolo: {self.titolo}\n"
                f"Autore: {self.autore}\n"
                f"Durata: {self.durata}\n"
                f"Numero Pagine: {self.numero_pagine}\n"
                f"Codice Attivazione: {self.codice_attivazione}\n"
                f"{'='*30}")

    def apri_libro(self):
        return f"Libro digitale '{self.titolo}' aperto con successo!"