print("Caricamento classe Podcast")

from Contenuto.contenuto import Contenuto

class Podcast(Contenuto):

    def __init__(self,titolo, autore, durata, ospite):
        super().__init__(titolo, autore, durata)
        self.ospite = ospite

    def __str__(self):
        return (f"\n{'='*30}\n"
                f"Titolo: {self.titolo}\n"
                f"Autore: {self.autore}\n"
                f"Durata: {self.durata}\n"
                f"Ospite: {self.ospite}\n"
                f"{'='*30}")

    def ascolta_podcast(self):
        return f"Podcast '{self.titolo}' ascoltato con successo!"