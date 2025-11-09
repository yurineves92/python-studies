# Classe simples
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos"

    def fazer_aniversario(self):
        self.idade += 1
        return f"Feliz aniversário! Agora tenho {self.idade} anos"
    
# Criar objetos
pessoa1 = Pessoa("Yuri", 32)
pessoa2 = Pessoa("Ana", 25)

print(pessoa1.apresentar())
print(pessoa2.apresentar())
print(pessoa1.fazer_aniversario())
