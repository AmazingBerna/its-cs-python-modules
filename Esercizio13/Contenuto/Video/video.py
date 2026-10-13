print("Caricamento classe Video")

from Contenuto.contenuto import Contenuto

class Video(Contenuto):

    def __init__(self,titolo, autore, durata, frame_rate, qualità, like, dislike):
        super().__init__(titolo, autore, durata)
        self.frame_rate = frame_rate
        self.qualità = qualità
        self.like = like
        self.dislike = dislike

    def __str__(self):
        return (f"\n{'='*30}\n"
                f"Titolo: {self.titolo}\n"
                f"Autore: {self.autore}\n"
                f"Durata: {self.durata}\n"
                f"Frame Rate: {self.frame_rate}\n"
                f"Qualità: {self.qualità}\n"
                f"Like: {self.like}\n"
                f"Dislike: {self.dislike}\n"
                f"{'='*30}")

    def guarda_video(self):
        return f"Video '{self.titolo}' riprodotto con successo!"