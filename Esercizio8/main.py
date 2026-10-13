print("Gestione veicoli")

from Veicolo import veicolo as V
from Veicolo import supports as S

lista_veicoli = []


def main():
    while True:
        print("\nMenu: ")
        print("1. Crea veicolo")
        print("2. Visualizza veicoli")
        print("3. Esci")
        scelta = int(input("Scegli un'opzione: "))
    
        match(scelta):
            case 1:
                marca = input("Inserisci la marca: ")
                modello = input("Inserisci il modello: ")
                anno = int(input("Inserisci l'anno: "))
                lista_veicoli.append(V.crea_veicolo(marca, modello, anno))
            case 2:
                S.visualizza_veicoli(lista_veicoli)
            case 3:
                break
            case _:
                print("Opzione non valida.")

if __name__ == "__main__":
    main()