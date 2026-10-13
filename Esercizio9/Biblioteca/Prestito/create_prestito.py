print("Prestiti generati casualmente")

import random
from datetime import date, timedelta
from Biblioteca.Prestito.prestito import Prestito
from Biblioteca.Libro.libro import Libro
from Biblioteca.Libro.create_libro import crea_libro
from Biblioteca.Utente.utente import Utente
from Biblioteca.Utente.create_user import crea_utente

def crea_prestito(Prestito):
    # Genera un utente e un libro random per il prestito
    libro = crea_libro(Libro)
    utente = crea_utente(Utente)
    
    # Genera una data di prestito casuale tra il 2020 e oggi (circa)
    giorni_dal_2020 = random.randint(0, 1000)
    data_prestito = date(2020, 1, 1) + timedelta(days=giorni_dal_2020)
    
    # Il prestito dura da 1 a 30 giorni
    durata_prestito = random.randint(1, 30)
    data_restituzione = data_prestito + timedelta(days=durata_prestito)
    
    return Prestito(libro, utente, data_prestito.strftime("%Y-%m-%d"), data_restituzione.strftime("%Y-%m-%d"))
