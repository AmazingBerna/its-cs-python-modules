print("Implementazione classe Figura")

class Figura:

    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return (f"\n{'='*30}\n"
                f"Nome: {self.nome}\n"
                f"{'='*30}")

print("\n\n"+"#"*50)
print("Testing classe Figura (SUPERCLASSE)")
print("#"*50)
