print("Benvenuto nel modulo di validazione")

def is_stringa(stringa):
    if (type(stringa) == str):
        print("La stringa è valida")
    else:
        print("La stringa non è valida")

def is_positive(numero):
    if(numero > 0):
        print("Il numero è positivo")
    else:
        print("Il numero non è positivo")

def is_valid_age(age):
    if(age >= 18 and age <= 65):
        print("L'età è valida")
    else:
        print("L'età non è valida")

def is_valid_email(email):
    if("@" in email):
        print("L'email è valida")
    else:
        print("L'email non è valida")

def is_valid_password(password):
    if(len(password) >= 8):
        print("La password è valida")
    else:
        print("La password non è valida")

    