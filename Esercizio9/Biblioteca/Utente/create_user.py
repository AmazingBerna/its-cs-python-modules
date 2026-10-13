print("Nomi utente generati casualmente")

import random
from random import choice as rc
from Biblioteca.Utente.utente import Utente

nomi = ["Alessandro", "Francesco", "Leonardo", "Lorenzo", "Matteo", "Riccardo", 
        "Gabriele", "Tommaso", "Federico", "Edoardo", "Giovanni", "Filippo", 
        "Giuseppe", "Antonio", "Marco", "Luca", "Diego", "Elia", "Liam", "Noah", 
        "Enea", "Zeno", "Milo", "Yuri", "Pietro", "Tancredi", "Giona", "Valerio", 
        "Aurelio", "Ludovico", "Orlando", "Dante", "Ettore", "Achille", "Claudio", 
        "Damiano", "Tiziano", "Vittorio", "Augusto", "Michele", "Samuele", "Daniele", 
        "Simone", "Stefano", "Christian", "Manuele", "Raffaele", "Davide", "Giacomo", 
        "Nicola", "Gabriel", "Nathan", "Iacopo", "Oliver", "Sebastian"]

cognomi = ["Rossi", "Russo", "Ferrari", "Esposito", "Bianchi", "Romano", 
            "Colombo", "Ricci", "Marino", "Greco", "Bruno", "Gallo", 
            "Conti", "De Luca", "Mancini", "Costa", "Giordano", "Rizzo", 
            "Lombardi", "Moretti", "Barbieri", "Fontana", "Santoro", "Mariani", 
            "Rinaldi", "Caruso", "Ferrara", "Galli", "Martini", "Leone", 
            "Guerra", "Rizzo", "Lombardi", "Moretti", "Barbieri", "Fontana", 
            "Santoro", "Mariani", "Rinaldi", "Caruso", "Ferrara", "Galli", 
            "Martini", "Leone", "Guerra", "Rizzo", "Lombardi", "Moretti", 
            "Barbieri", "Fontana", "Santoro", "Mariani", "Rinaldi", "Caruso", 
            "Ferrara", "Galli", "Martini", "Leone", "Guerra", "Rizzo", 
            "Lombardi", "Moretti", "Barbieri", "Fontana", "Santoro", "Mariani", 
            "Rinaldi", "Caruso", "Ferrara", "Galli", "Martini", "Leone", 
            "Guerra", "Rizzo", "Lombardi", "Moretti", "Barbieri", "Fontana", 
            "Santoro", "Mariani", "Rinaldi", "Caruso", "Ferrara", "Galli", 
            "Martini", "Leone", "Guerra", "Rizzo", "Lombardi", "Moretti", 
            "Barbieri", "Fontana", "Santoro", "Mariani", "Rinaldi", "Caruso", 
            "Ferrara", "Galli", "Martini", "Leone", "Guerra", "Rizzo", 
            "Lombardi", "Moretti", "Barbieri", "Fontana", "Santoro", "Mariani", 
            "Rinaldi", "Caruso", "Ferrara", "Galli", "Martini", "Leone", 
            "Guerra", "Rizzo", "Lombardi", "Moretti", "Barbieri", "Fontana", 
            "Santoro", "Mariani", "Rinaldi", "Caruso", "Ferrara", "Galli", 
            "Martini", "Leone", "Guerra", "Rizzo", "Lombardi", "Moretti", 
            "Barbieri", "Fontana", "Santoro", "Mariani", "Rinaldi", "Caruso", 
            "Ferrara", "Galli", "Martini", "Leone", "Guerra", "Rizzo", 
            "Lombardi", "Moretti", "Barbieri", "Fontana", "Santoro", "Mariani", 
            "Rinaldi", "Caruso", "Ferrara", "Galli", "Martini", "Leone", 
            "Guerra", "Rizzo", "Lombardi", "Moretti", "Barbieri", "Fontana", 
            "Santoro", "Mariani", "Rinaldi", "Caruso", "Ferrara", "Galli", 
            "Martini", "Leone", "Guerra", "Rizzo", "Lombardi", "Moretti", 
            "Barbieri", "Fontana", "Santoro", "Mariani", "Rinaldi", "Caruso", 
            "Ferrara", "Galli", "Martini", "Leone", "Guerra", "Rizzo", 
            "Lombardi", "Moretti", "Barbieri", "Fontana", "Santoro", "Mariani", 
            "Rinaldi", "Caruso", "Ferrara", "Galli", "Martini", "Leone", 
            "Guerra", "Rizzo", "Lombardi", "Moretti", "Barbieri", "Fontana", 
            "Santoro", "Mariani", "Rinaldi", "Caruso", "Ferrara", "Galli", 
            "Martini", "Leone", "Guerra", "Rizzo", "Lombardi", "Moretti", 
            "Barbieri", "Fontana", "Santoro", "Mariani", "Rinaldi", "Caruso", 
            "Ferrara", "Galli", "Martini", "Leone", "Guerra", "Rizzo", 
            "Lombardi", "Moretti", "Barbieri", "Fontana", "Santoro", "Mariani", 
            "Rinaldi", "Caruso", "Ferrara", "Galli", "Martini", "Leone", 
            "Guerra", "Rizzo", "Lombardi", "Moretti", "Barbieri", "Fontana", 
            "Santoro", "Mariani", "Rinaldi", "Caruso", "Ferrara", "Galli", 
            "Martini", "Leone", "Guerra", "Rizzo", "Lombardi", "Moretti", 
            "Barbieri", "Fontana", "Santoro", "Mariani", "Rinaldi", "Caruso", 
            "Ferrara", "Galli", "Martini", "Leone", "Guerra", "Rizzo", 
            "Lombardi", "Moretti", "Barbieri", "Fontana", "Santoro", "Mariani", 
            "Rinaldi", "Caruso", "Ferrara", "Galli", "Martini", "Leone", 
            "Guerra", "Rizzo", "Lombardi", "Moretti", "Barbieri", "Fontana", 
            "Santoro", "Mariani", "Rinaldi", "Caruso", "Ferrara", "Galli", 
            "Martini", "Leone", "Guerra", "Rizzo", "Lombardi", "Moretti", 
            "Barbieri", "Fontana", "Santoro", "Mariani", "Rinaldi", "Caruso", 
            "Ferrara", "Galli", "Martini", "Leone", "Guerra", "Rizzo", 
            "Lombardi", "Moretti", "Barbieri", "Fontana", "Santoro", "Mariani", 
            "Rinaldi", "Caruso", "Ferrara", "Galli", "Martini", "Leone", 
            "Guerra", "Rizzo", "Lombardi", "Moretti", "Barbieri", "Fontana", 
            "Santoro", "Mariani", "Rinaldi", "Caruso", "Ferrara", "Galli", 
            "Martini", "Leone", "Guerra", "Rizzo", "Lombardi", "Moretti", 
            "Barbieri", "Fontana", "Santoro", "Mariani", "Rinaldi", "Caruso", 
            "Ferrara", "Galli", "Martini", "Leone", "Guerra", "Rizzo", 
            "Lombardi", "Moretti", "Barbieri", "Fontana", "Santoro", "Mariani", 
            "Rinaldi", "Caruso", "Ferrara", "Galli", "Martini", "Leone", 
            "Guerra", "Rizzo", "Lombardi", "Moretti", "Barbieri", "Fontana", 
            "Santoro", "Mariani", "Rinaldi", "Caruso", "Ferrara", "Galli", 
            "Martini", "Leone", "Guerra", "Rizzo", "Lombardi", "Moretti", 
            "Barbieri", "Fontana", "Santoro", "Mariani", "Rinaldi", "Caruso", 
            "Ferrara", "Galli", "Martini", "Leone", "Guerra", "Rizzo", 
            "Lombardi", "Moretti", "Barbieri", "Fontana", "Santoro", "Mariani", 
            "Rinaldi", "Caruso", "Ferrara", "Galli", "Martini", "Leone", 
            "Guerra", "Rizzo", "Lombardi", "Moretti", "Barbieri", "Fontana", 
            "Santoro"]

strade = ["Via Roma","Corso Vittorio Emanuele II","Viale dei Ciliegi","Piazza del Popolo",
            "Largo Argentina","Via della Conciliazione","Corso Buenos Aires","Viale della Libertà",
            "Via dei Mille","Piazza di Spagna","Viale Regina Margherita","Via Dante Alighieri",
            "Corso Garibaldi","Via Montenapoleone","Piazza Navona","Viale dei Fori Imperiali",
            "Via del Corso","Corso Italia","Via Veneto","Piazza Duomo","Viale delle Milizie",
            "Via Appia Nuova","Corso Francia","Via Torino","Piazza San Marco","Viale Monza",
            "Via dei Condotti","Corso Porta Nuova","Via Merulana Parioli","Piazza della Signoria",
            "Viale Trastevere Parioli","Via XX Settembre","Corso Umberto I","Via del Tritone Parioli",
            "Piazza Castello","Viale Mazzini Parioli","Via Andrea Doria","Corso Sempione",
            "Via Etnea","Piazza De Ferrari","Viale Europa Parioli","Via Nazionale Parioli",
            "Corso Ruggero","Via Caracciolo","Piazza Plebiscito Parioli","Viale Gramsci Parioli",
            "Via Chiaia Parioli","Corso Palladio","Via Zamboni Parioli","Piazza Bra Parioli"]

def crea_utente(Utente):
    nome =  (nomi)
    cognome = rc(cognomi)

    eta = random.randint(18, 90)

    email = f"{nome}.{cognome}{eta}@email.com"
    telefono = random.randint(1234567890, 9999999999)
    indirizzo = f"{rc(strade)} {random.randint(1, 100)}"

    return Utente(nome, cognome, eta, email, telefono, indirizzo)