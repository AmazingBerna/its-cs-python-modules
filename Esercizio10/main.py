print("Gestione di un negozio")

from Carrello.chest import Chest
from Prodotto.product import Product as prod

lista_prodotti = [prod("Mela", 1, 10), prod("Banana", 2, 20), prod("Arancia", 3, 30), prod("Pera", 4, 40), prod("Uva", 5, 50), 
                prod("Ananas", 6, 60), prod("Mango", 7, 70), prod("Kiwi", 8, 80), prod("Fragola", 9, 90), prod("Mirtillo", 10, 100),
                prod("Lampone", 11, 110), prod("Mora", 12, 120), prod("Ribes", 13, 130), prod("Ciliegia", 14, 140), prod("Albicocca", 15, 150),
                prod("Pesca", 16, 160), prod("Prugna", 17, 170), prod("Susina", 18, 180), prod("Fico", 19, 190), prod("Melone", 20, 200),
                prod("Anguria", 21, 210), prod("Cocomero", 22, 220), prod("Mandarino", 23, 230), prod("Pompelmo", 24, 240), prod("Limone", 25, 250),
                prod("Lime", 26, 260)]

carrello = Chest([])

print("LISTA PRODOTTI DISPONIBILI")
print("-" * 50)
for prodotto in lista_prodotti:
    print(f"| Nome: {prodotto.nome} | Prezzo: {prodotto.prezzo} | Quantità: {prodotto.quantita} |")
print("-" * 50)

while True:
    print("---Menù---")
    print("1. Aggiungi prodotto al carrello")
    print("2. Rimuovi prodotto dal carrello")
    print("3. Mostra carrello")
    print("4. Svuota carrello")
    print("5. Calcola totale")
    print("6. Esci")
    scelta = int(input("Scegli un'opzione: "))
    
    match(scelta):
        case 1:
            nome = input("Nome del prodotto: ")
            for p in lista_prodotti:
                if p.nome == nome:
                    quantita = int(input("Inserisci la quantità: "))
                    carrello.add_product(prod(nome, p.prezzo, quantita))
                    break
            else:
                print(f"Prodotto '{nome}' non trovato nella lista.")

        case 2:
            nome = input("Nome del prodotto: ")
            carrello.remove_product(nome)
        
        case 3:
            carrello.show_chest()
        
        case 4:
            carrello.empty_chest()
        
        case 5:
            print("Il totale del carrello è: ", carrello.calculate_total())
        
        case 6:
            break
        
        case _:
            print("Scelta non valida")
        