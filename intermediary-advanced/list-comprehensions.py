# Criar lista de quadrados
quadrados = [x**2 for x in range(1, 11)]
print(f"Quadrados: {quadrados}")

# Com condição
pares = [x for x in range(1, 21) if x % 2 == 0]
print(f"Pares: {pares}")

# Nested comprehension
matriz = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print("Matriz:")
for linha in matriz:
    print(linha)

# Transformaras strings
nomes = ['João', "Maria", "Pedro"]
nomes_capitalizados = [nome.capitalize() for nome in nomes]
print(f"Nomes: {nomes_capitalizados}")