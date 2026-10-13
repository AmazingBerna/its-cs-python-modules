print("main")
from Lib.random import randint
from utilita.numeri.max_num import max_num as max
from utilita.numeri.media_lista import media_lista as media
from utilita.testo.conta_vocali import conta_vocali as conta_vocali
from utilita.testo.palindromo import is_palindromo as is_palindromo

def menu():
    print("\n1. Trova il massimo in una lista di numeri")
    print("2. Calcola la media di una lista di numeri")
    print("3. Conta le vocali in una stringa")
    print("4. Verifica se una stringa è palindroma")
    print("5. Esci")
    scelta = int(input("Scegli un'opzione: "))
    return scelta

def main():
    while True:
        scelta = menu()
        match(scelta):
            case 1:
                N = int(input("Quanti numeri vuoi inserire? "))
                lista = []
                for _ in range(N):
                    lista.append(randint(1,100))
                print(f"La lista è: {lista}")
                print(f"Il massimo è: {max(lista)}")
            case 2:
                N = int(input("Quanti numeri vuoi inserire? "))
                lista = []
                for _ in range(N):
                    lista.append(randint(1,100))
                print(f"La lista è: {lista}")
                print(f"La media è: {media(lista)}")
            case 3:
                testo = input("Inserisci una stringa: ")
                print(f"La stringa è: {testo}")
                print(f"Le vocali sono: {conta_vocali(testo)}")
            case 4:
                testo = input("Inserisci una stringa: ")
                print(f"La stringa è: {testo}")
                print(f"Le vocali sono: {is_palindromo(testo)}")
            case 5:
                break
            case _:
                print("Scelta non valida")

if __name__ == "__main__":
    main()