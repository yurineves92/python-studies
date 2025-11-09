import numpy as np

# Criar arrays
arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}")

# Operações
print(f"Soma: {arr.sum()}")
print(f"Média: {arr.mean()}")
print(f"Máximo: {arr.max()}")

# Array 2d
matriz = np.array([[1,2,3], [4,5,6]])
print(f"Matriz:\n{matriz}")
print(f"Shape: {matriz.shape}")

# Operações matemáticas
print(f"Multiplicar por 2:\n{matriz * 2}")