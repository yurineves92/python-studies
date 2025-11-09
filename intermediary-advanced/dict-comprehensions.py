# Criar dicionário de quadrados
quadrados_dict = {x: x**2 for x in range(1,6)}
print(f"Quadrados: {quadrados_dict}")

# Inverter dicionário
original = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original.items()}
print(f"Invertido: {invertido}")

# Com condição
numeros = {"a":1, "b": 2, "c": 3, "d":4, "e":5}
pares = {k: v for k, v in numeros.items() if v % 2 == 0}
impares = {k: v for k, v in numeros.items() if v % 2 == 1}
print(f"Pares: {pares}")
print(f"Impares: {impares}")