print("Import selettivo")

def conta_caratteri(stringa):
    """Restituisce il numero di caratteri di una stringa."""
    return len(stringa)

def maiuscolo(stringa):
    """Restituisce la stringa in maiuscolo."""
    return stringa.upper()

def cerca_parola(stringa, parola):
    """Restituisce True se la parola è presente nella stringa, False altrimenti."""
    return parola in stringa

def inverti_stringa(stringa):
    """Restituisce la stringa invertita."""
    return stringa[::-1]