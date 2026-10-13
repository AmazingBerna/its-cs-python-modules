def menu():
    print("\n" + "=" * 30)
    print("CALCOLATRICE AVANZATA")
    print("=" * 30)
    print("1. Operazioni di base")
    print("2. Operazioni avanzate")
    print("3. Esci")
    print("=" * 30)
    return input("Scegli un'operazione: ")

def menu_base():
    print("\n" + "=" * 30)
    print("OPERAZIONI DI BASE")
    print("=" * 30)
    print("1. Addizione")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Divisione")
    print("5. Esci")
    print("=" * 30)

def menu_avanzate():
    print("\n" + "=" * 30)
    print("OPERAZIONI AVANZATE")
    print("=" * 30)
    print("1. Potenza")
    print("2. Radice quadrata")
    print("3. Fattoriale")
    print("4. Massimo Comun Divisore")
    print("5. Minimo Comune Multiplo")
    print("6. Verifica numero primo")
    print("7. Sequenza di Fibonacci")
    print("8. Equazione di secondo grado")
    print("9. Media")
    print("10. Esci")
    print("=" * 30)

def leggi_numero(messaggio):
    """Richiede all'utente di inserire un numero valido."""
    while True:
        valore = input(messaggio)
        try:
            num = float(valore)
            return int(num) if num.is_integer() else num
        except ValueError:
            print("Errore: devi inserire un numero valido. Riprova.")

def mostra_risultato(messaggio):
    """Mostra l'output o il risultato in un formato chiaro."""
    print(f"\n{messaggio}")