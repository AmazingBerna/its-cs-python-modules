print("Registrazione utente")

import validatori as val

def main():
    nome = input("Inserisci il tuo nome: ")
    val.is_stringa(nome)

    age = int(input("Inserisci la tua età: "))
    val.is_valid_age(age)

    email = input("Inserisci la tua email: ")
    val.is_valid_email(email)

    password = input("Inserisci la tua password: ")
    val.is_valid_password(password)

if __name__ == "__main__":
    main()