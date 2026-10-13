print("Caricamento classe Libro")

class Libro:

    def __init__(self, titolo, autore, anno, editore, genere,):

        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.editore = editore
        self.genere = genere
        self.disponibile = True
    
    def __str__(self):
        return f"Titolo: {self.titolo}\nAutore: {self.autore}\nAnno: {self.anno}\nEditore: {self.editore}\nGenere: {self.genere}\nDisponibile: {self.disponibile}"