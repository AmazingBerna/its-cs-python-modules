import base_operations as bo
import hard_operations as ho 
import gestioneIO as io

def main():
    
    while True:

        match io.menu():
            
            case "1":
                io.menu_base()
                scelta = input("Scegli un'operazione: ")

                try:
                    match(scelta):
                        case "1":
                            num1 = io.leggi_numero("Inserisci il primo numero: ")
                            num2 = io.leggi_numero("Inserisci il secondo numero: ")
                            io.mostra_risultato(f"La somma di {num1} e {num2} è {bo.add(num1, num2)}")            
                        case "2":
                            num1 = io.leggi_numero("Inserisci il primo numero: ")
                            num2 = io.leggi_numero("Inserisci il secondo numero: ")
                            io.mostra_risultato(f"La differenza tra {num1} e {num2} è {bo.subtract(num1, num2)}")
                        case "3":
                            num1 = io.leggi_numero("Inserisci il primo numero: ")
                            num2 = io.leggi_numero("Inserisci il secondo numero: ")
                            io.mostra_risultato(f"Il prodotto di {num1} e {num2} è {bo.multiply(num1, num2)}")
                        case "4":
                            num1 = io.leggi_numero("Inserisci il primo numero: ")
                            num2 = io.leggi_numero("Inserisci il secondo numero: ")
                            io.mostra_risultato(f"Il quoziente tra {num1} e {num2} è {bo.divide(num1, num2)}")
                        case "5":
                            break
                        case _:
                            io.mostra_risultato("Scelta non valida. Riprova.")
                except Exception as e:
                    io.mostra_risultato(f"Errore matematico: {e}")

            case "2":
                io.menu_avanzate()
                scelta = input("Scegli un'operazione: ")
                
                try:
                    match(scelta):
                        case "1":
                            base = io.leggi_numero("Inserisci la base: ")
                            esponente = io.leggi_numero("Inserisci l'esponente: ")
                            io.mostra_risultato(f"La potenza di {base} elevata a {esponente} è {ho.power(base, esponente)}")
                        case "2":
                            numero = io.leggi_numero("Inserisci il numero: ")
                            io.mostra_risultato(f"La radice quadrata di {numero} è {ho.square_root(numero)}")
                        case "3":
                            numero = io.leggi_numero("Inserisci il numero: ")
                            io.mostra_risultato(f"Il fattoriale di {numero} è {ho.factorial(numero)}")
                        case "4":
                            num1 = io.leggi_numero("Inserisci il primo numero: ")
                            num2 = io.leggi_numero("Inserisci il secondo numero: ")
                            io.mostra_risultato(f"Il Massimo Comun Divisore tra {num1} e {num2} è {ho.gcd(num1, num2)}")
                        case "5":
                            num1 = io.leggi_numero("Inserisci il primo numero: ")
                            num2 = io.leggi_numero("Inserisci il secondo numero: ")
                            io.mostra_risultato(f"Il Minimo Comune Multiplo tra {num1} e {num2} è {ho.lcm(num1, num2)}")
                        case "6":
                            numero = io.leggi_numero("Inserisci il numero: ")
                            io.mostra_risultato(f"Il numero {numero} è primo? {ho.is_prime(numero)}")
                        case "7":
                            numero = io.leggi_numero("Inserisci il numero: ")
                            io.mostra_risultato(f"L'n-esimo numero della sequenza di Fibonacci è {ho.fibonacci(numero)}")
                        case "8":
                            a = io.leggi_numero("Inserisci il coefficiente a: ")
                            b = io.leggi_numero("Inserisci il coefficiente b: ")
                            c = io.leggi_numero("Inserisci il coefficiente c: ")
                            io.mostra_risultato(f"Le radici dell'equazione di secondo grado sono {ho.solve_quadratic(a, b, c)}")
                        case "9":
                            numeri = []
                            io.mostra_risultato("Media. Inserisci i numeri uno alla volta (lascia vuoto per terminare).")
                            while True:
                                num_str = input("Numero: ")
                                if num_str.strip() == "":
                                    break
                                try:
                                    n = float(num_str)
                                    numeri.append(int(n) if n.is_integer() else n)
                                except ValueError:
                                    print("Ignorato. Non è un numero valido.")
                            io.mostra_risultato(f"La media è {ho.average(*numeri)}")
                        case "10":
                            break
                        case _:
                            io.mostra_risultato("Scelta non valida. Riprova.")
                except Exception as e:
                    io.mostra_risultato(f"Errore matematico: {e}")
            case "3":
                break
            case _:
                io.mostra_risultato("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()