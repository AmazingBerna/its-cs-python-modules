print("\nImport selettivo")

from import_selettivo import conta_caratteri as cc
print("Il numero di caratteri di 'ciao' è: " + str(cc("ciao")))

import import_selettivo as Is
print("La stringa 'ciao' in maiuscolo è: " + Is.maiuscolo("ciao"))

from import_selettivo import cerca_parola
print("La parola 'ciao' è presente nella stringa 'ciao'?: " + str(cerca_parola("ciao", "ciao")))

from import_selettivo import inverti_stringa as invs
print("La stringa 'ciao' invertita è: " + invs("ciao"))