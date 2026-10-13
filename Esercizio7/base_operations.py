# ==========================================
# Operazioni Matematiche Semplici
# ==========================================

def add(a, b):
    """Restituisce la somma di a e b."""
    return a + b

def subtract(a, b):
    """Restituisce la differenza tra a e b."""
    return a - b

def multiply(a, b):
    """Restituisce il prodotto di a e b."""
    return a * b

def divide(a, b):
    """Restituisce il quoziente tra a e b. Solleva un'eccezione se b è zero."""
    if b == 0:
        raise ValueError("Impossibile dividere per zero.")
    return a / b