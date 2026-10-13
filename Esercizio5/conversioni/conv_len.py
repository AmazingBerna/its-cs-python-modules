print("conv_lunghezze module loaded")

def menu():
    print("1. Metri in centimetri")
    print("2. Pollici in centimetri")
    print("3. Chilometri in miglia")
    print("4. Esci")

    scelta = int(input("Scegli una conversione: "))

    match(scelta):
        case 1:
            metri_in_centimetri(float(input("Inserisci i metri: ")))
        case 2:
            pollici_in_centimetri(float(input("Inserisci i pollici: ")))
        case 3:
            chilometri_in_miglia(float(input("Inserisci i chilometri: ")))
        case 4:
            exit()
        case _:
            print("Scelta non valida")

def metri_in_centimetri(metri):
    print(f"{metri} metri sono {metri * 100} centimetri")

def pollici_in_centimetri(pollici):
    print(f"{pollici} pollici sono {pollici * 2.54} centimetri")

def chilometri_in_miglia(km):
    print(f"{km} chilometri sono {km * 0.621371} miglia")

def miglia_in_chilometri(miglia):
    print(f"{miglia} miglia sono {miglia / 0.621371} chilometri")
