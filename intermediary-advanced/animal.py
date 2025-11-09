# Classe base
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        pass

    def apresentar(self):
        return f"Eu sou {self.nome}"

# Classes derivadas
class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"
    
    def buscar_bola(self):
        return f"{self.nome} está buscando a bola!"
    
class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

    def arranhar(self):
        return f"{self.nome} está arranhando!"

# Usar as classes

rex = Cachorro("Rex")
mimi = Gato("Mimi")

print(rex.apresentar())
print(rex.fazer_som())
print(rex.buscar_bola())

print(mimi.apresentar())
print(mimi.fazer_som())
print(mimi.arranhar())