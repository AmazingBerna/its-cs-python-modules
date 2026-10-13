import gestioneIO as IO
import logica as LOG

while True:
    print("\n")
    print("---Menù---")
    print("1. Calcola area rettangolo")
    print("2. Calcola perimetro rettangolo")
    print("3. Convertire da Celsius a Fahrenheit")
    print("4. Esci")

    scelta = IO.leggi_scelta()


    match(scelta):
        case 1:
            #area rettangolo
            base = IO.leggi_numero("Inserisci la base del rettangolo: ")
            altezza = IO.leggi_numero("Inserisci l'altezza del rettangolo: ")
            area = LOG.area_rettangolo(base, altezza)
            IO.mostra_risultato(f"L'area del rettangolo è: {area}")
        case 2:
            #perimetro rettangolo
            base = IO.leggi_numero("Inserisci la base del rettangolo: ")
            altezza = IO.leggi_numero("Inserisci l'altezza del rettangolo: ")
            perimetro = LOG.perimetro_rettangolo(base, altezza)
            IO.mostra_risultato(f"Il perimetro del rettangolo è: {perimetro}")
        case 3:
            #conversione celsius fahrenheit
            celsius = IO.leggi_numero("Inserisci i gradi Celsius: ")
            fahrenheit = LOG.celsius_a_fahrenheit(celsius)
            IO.mostra_risultato(f"{celsius}°C corrispondono a {fahrenheit}°F")  
        case 4:
            #uscita
            IO.mostra_risultato("Arrivederci!")
            break
        case _:
            #errore
            IO.mostra_risultato("Scelta non valida")
