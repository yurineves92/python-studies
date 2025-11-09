# Generator function
def contador(maximo):
    n = 0
    while n < maximo:
        yield n
        n += 1

# Usar Generator
for num in contador(5):
    print(num)

# Generator expression
quadrados_gen = (x**2 for x in range(1,6))
print(f"Tipo: {type(quadrados_gen)}")
for quad in quadrados_gen:
    print(quad)

# Generator para Fibonacci
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a +b

print("Fibonacci:")
for num in fibonacci(10):
    print(num, end=" ")
print()
