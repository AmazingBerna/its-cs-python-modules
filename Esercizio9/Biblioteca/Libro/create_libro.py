print("Libri generati casualmente")

import random
from random import choice as rc
from Biblioteca.Libro.libro import Libro

titoli = [
    "Il Signore degli Anelli", "1984", "Il Piccolo Principe", 
    "Il Nome della Rosa", "Don Chisciotte", "Moby Dick", 
    "Orgoglio e Pregiudizio", "Guerra e Pace", "La Divina Commedia", 
    "Odissea", "I Promessi Sposi", "Decameron", "Fahrenheit 451",
    "Il ritratto di Dorian Gray", "Il fu Mattia Pascal", "Dracula"
]

autori = [
    "J.R.R. Tolkien", "George Orwell", "Antoine de Saint-Exupéry", 
    "Umberto Eco", "Miguel de Cervantes", "Herman Melville", 
    "Jane Austen", "Lev Tolstoj", "Dante Alighieri", 
    "Omero", "Alessandro Manzoni", "Giovanni Boccaccio", "Ray Bradbury",
    "Oscar Wilde", "Luigi Pirandello", "Bram Stoker"
]

editori = [
    "Mondadori", "Einaudi", "Feltrinelli", "Bompiani", "Rizzoli", 
    "Boringhieri", "Zanichelli", "Adelphi", "Garzanti", "Sellerio",
    "Newton Compton", "Fazi Editore", "Sperling & Kupfer"
]

generi = [
    "Fantasy", "Fantascienza", "Romanzo", "Giallo", "Storico", 
    "Poesia", "Avventura", "Epico", "Classico", "Thriller", "Horror"
]

def crea_libro(Libro):
    titolo = rc(titoli)
    autore = rc(autori)
    anno = random.randint(1800, 2024)
    editore = rc(editori)
    genere = rc(generi)

    return Libro(titolo, autore, anno, editore, genere)
