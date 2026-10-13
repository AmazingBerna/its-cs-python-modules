print("Ereditarietà semplice")

from Dipendente import Dipendente as D
from Sviluppatore import Sviluppatore as S
from Designer import Designer as Des

dipendente1 = D("Mario", "Rossi", "[EMAIL_ADDRESS]", 1, 1000)
dipendente2 = S("Luigi", "Bianchi", "[EMAIL_ADDRESS]", 2, 2000, "Python", "VS Code")
dipendente3 = Des("Paolo", "Verdi", "[EMAIL_ADDRESS]", 3, 3000, "Python", "Photoshop")

print(dipendente1)
print(dipendente2)
print(dipendente3)

