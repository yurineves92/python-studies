def soma_todos(*args):
    return sum(args)

print(f"Soma: {soma_todos(1,2,3,4,5,6)}")

def exibir_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exibir_info(nome = "Yuri", idade = 32, cidade = "Curitiba")

# Função lambda
quadrado = lambda x: x ** 2
print(f"Quadrado de 5: {quadrado(5)}")

# Lambda com map
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x**2, numeros))
print(f"Quadrados: {quadrados}")

# Lambda com filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Pares: {pares}")