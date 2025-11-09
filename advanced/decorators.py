# Decorator simples
def meu_decorator(func):
    def wrapper():
        print("Antes da função")
        func()
        print("Depois da função")
    return wrapper

@meu_decorator
def dizer_ola():
    print("Olá!")

dizer_ola()

# Decorator com argumentos
def repetir(vezes):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(vezes):
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorator

@repetir(3)
def saudacao(nome):
    print(f"Olá, {nome}")

saudacao("Yuri")

# Decorator para medir tempo
import time

def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tempo
def processar_dados():
    time.sleep(1)
    return "Processamento concluído"

print(processar_dados())