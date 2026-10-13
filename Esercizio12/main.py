print("Test Figure Geometriche")

from Figura.figura import Figura as F
from Figura.Rettangolo.rettangolo import Rettangolo as R
from Figura.Triangolo.triangolo import Triangolo as T
from Figura.Cerchio.cerchio import Cerchio as C


scelta = input("Inserisci il tipo di figura: ")

match(scelta):
    case "rettangolo":
        b = int(input("Inserisci la base: "))
        a = int(input("Inserisci l'altezza: "))
        rettangolo = R("rettangolo", b, a)
        print(rettangolo)
    case "triangolo":
        b = int(input("Inserisci la base: "))
        a = int(input("Inserisci l'altezza: "))
        triangolo = T("triangolo", b, a)
        print(triangolo)
    case "cerchio":
        r = int(input("Inserisci il raggio: "))
        cerchio = C("cerchio", r)
        print(cerchio)
    case _:
        print("figura non valida")