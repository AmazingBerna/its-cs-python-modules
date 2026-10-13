from Biblioteca.Libro.libro import Libro
from Biblioteca.Utente.utente import Utente
from Biblioteca.Prestito.prestito import Prestito

from Biblioteca.Libro.create_libro import crea_libro
from Biblioteca.Utente.create_user import crea_utente
from Biblioteca.Prestito.create_prestito import crea_prestito

def menu():
    libri = []
    utenti = []
    prestiti = []

    while True:
        print("\n" + "="*45)
        print("             MENU BIBLIOTECA             ")
        print("="*45)
        print(" 1. Genera e aggiungi Utenti")
        print(" 2. Genera e aggiungi Libri")
        print(" 3. Genera e aggiungi Prestiti")
        print(" 4. Visualizza tutti gli Utenti generati")
        print(" 5. Visualizza tutti i Libri generati")
        print(" 6. Visualizza tutti i Prestiti generati")
        print(" 0. Esci dal programma")   
        print("="*45)
        
        scelta = input("Seleziona un'opzione: ")

        match scelta:
            case '1':
                try:
                    num = int(input("Quanti utenti casuali vuoi generare? "))
                    for _ in range(num):
                        utenti.append(crea_utente(Utente))
                    print(f"\n--> {num} utenti generati con successo!")
                except ValueError:
                    print("\nErrore: Inserisci un numero valido.")
            
            case '2':
                try:
                    num = int(input("Quanti libri casuali vuoi generare? "))
                    for _ in range(num):
                        libri.append(crea_libro(Libro))
                    print(f"\n--> {num} libri generati con successo!")
                except ValueError:
                    print("\nErrore: Inserisci un numero valido.")
                    
            case '3':
                try:
                    num = int(input("Quanti prestiti casuali vuoi generare? "))
                    for _ in range(num):
                        prestiti.append(crea_prestito(Prestito))
                    print(f"\n--> {num} prestiti generati con successo!")
                except ValueError:
                    print("\nErrore: Inserisci un numero valido.")
                    
            case '4':
                print("\n" + "-"*45)
                print("                ELENCO UTENTI                ")
                print("-"*45)
                if not utenti:
                    print("Nessun utente presente. Generane prima alcuni.")
                else:
                    for i, u in enumerate(utenti, 1):
                        print(f"\n[Utente {i}]")
                        # La classe ha il suo metodo __str__
                        print(u)
                print("-"*45)
                
            case '5':
                print("\n" + "-"*45)
                print("                 ELENCO LIBRI                ")
                print("-"*45)
                if not libri:
                    print("Nessun libro presente. Generane prima alcuni.")
                else:
                    for i, l in enumerate(libri, 1):
                        print(f"\n[Libro {i}]")
                        print(l)
                print("-"*45)
                
            case '6':
                print("\n" + "-"*45)
                print("               ELENCO PRESTITI               ")
                print("-"*45)
                if not prestiti:
                    print("Nessun prestito presente. Generane prima alcuni.")
                else:
                    for i, p in enumerate(prestiti, 1):
                        print(f"\n[Prestito {i}]")
                        print(p)
                print("-"*45)
                
            case '0':
                print("\nChiusura del programma in corso... Arrivederci!")
                break
                
            case _:
                print("\nScelta non valida! Digita un numero compreso tra 0 e 6.")

if __name__ == "__main__":
    menu()
