def leggi_scelta():
    """Richiede all'utente di effettuare una scelta e la converte in intero."""
    scelta = input("\nScegli un'opzione: ")
    try:
        return int(scelta)
    except ValueError:
        return -1  # Ritorna un valore che indicherà un errore

def leggi_numero(messaggio):
    """Richiede all'utente di inserire un numero valido."""
    while True:
        valore = input(messaggio)
        try:
            return float(valore)
        except ValueError:
            print("Errore: devi inserire un numero valido. Riprova.")

def mostra_risultato(messaggio):
    """Mostra l'output o il risultato in un formato chiaro."""
    print(f"\n{messaggio}")
