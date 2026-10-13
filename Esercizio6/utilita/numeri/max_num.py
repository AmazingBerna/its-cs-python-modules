def max_num(lista):
    massimo = lista[0]
    for i in lista:
        if i > massimo:
            massimo = i
    return massimo