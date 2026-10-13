import math
import cmath

# ==========================================
# Operazioni Matematiche Avanzate
# ==========================================

def power(base, exponent):
    """Restituisce la base elevata all'esponente."""
    return math.pow(base, exponent)

def square_root(x):
    """Restituisce la radice quadrata di x."""
    if x < 0:
        raise ValueError("Impossibile calcolare la radice quadrata di un numero negativo nei numeri reali.")
    return math.sqrt(x)

def factorial(n):
    """Restituisce il fattoriale di n."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Il numero deve essere un intero non negativo.")
    return math.factorial(n)

def gcd(a, b):
    """Restituisce il Massimo Comun Divisore (MCD) tra a e b."""
    return math.gcd(a, b)

def lcm(a, b):
    """Restituisce il Minimo Comune Multiplo (mcm) tra a e b."""
    return abs(a * b) // math.gcd(a, b) if a and b else 0

def is_prime(n):
    """Verifica se un numero è primo."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def fibonacci(n):
    """Restituisce l'n-esimo numero della sequenza di Fibonacci."""
    if n < 0:
        raise ValueError("n non può essere negativo.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def solve_quadratic(a, b, c):
    """
    Risolve un'equazione di secondo grado della forma ax^2 + bx + c = 0.
    Restituisce una tupla con le due radici (reali o complesse).
    """
    if a == 0:
        raise ValueError("Il coefficiente 'a' non può essere zero.")
    
    discriminant = (b**2) - (4*a*c)
    
    root1 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b + cmath.sqrt(discriminant)) / (2*a)
    
    # Ritorna numeri reali se la parte immaginaria è nulla
    def format_root(root):
        if root.imag == 0:
            return root.real
        return root
            
    return format_root(root1), format_root(root2)

def average(*numbers):
    """
    Calcola la media tra più numeri forniti.
    Accetta un numero variabile di argomenti, es. average(1, 2, 3, 4).
    """
    if not numbers:
        raise ValueError("Nessun numero fornito. Inserire almeno un numero.")
    return sum(numbers) / len(numbers)