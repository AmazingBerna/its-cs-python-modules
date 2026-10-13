def visualizza_veicoli(lista_veicoli):
    """Stampa a schermo tutti i veicoli presenti nella lista."""
    if not lista_veicoli:
        print("Nessun veicolo presente.")
        return
    for veicolo in lista_veicoli:
        print(veicolo)
