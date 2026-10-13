print("Inserimento dati prodotto")

import validatori as val

def main():
    nome = input("Inserisci il nome del prodotto: ")
    val.is_stringa(nome)

    prezzo = float(input("Inserisci il prezzo del prodotto: "))
    val.is_positive(prezzo)

    quantita = int(input("Inserisci la quantità del prodotto: "))
    val.is_positive(quantita)

if __name__ == "__main__":
    main()