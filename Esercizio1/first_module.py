print("Primo modulo")

def somma(a,b):
    return a+b

def moltiplicazione(a, b):
    """Restituisce il prodotto di a per b."""
    return a * b

def pari_dispari(a):
    """Restituisce 'pari' se il numero è pari, 'dispari' se è dispari."""
    if a % 2 == 0:
        return "pari"
    else:
        return "dispari"
