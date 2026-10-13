from math import ceil

def is_palindromo(testo):

    for i in range(ceil((len(testo)/2))):
        if testo[i] != testo[len(testo)-i-1]:
            return False
    return True

    