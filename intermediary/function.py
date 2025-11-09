# Função simples
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Yuri"))

# Função com múltiplos parâmetros
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media

resultado  = calcular_media(8.5, 9.0, 7.5)
print(f"Média: {resultado:.2f}")

# Função com valor padrão
def potencia(base, expoente = 2):
    return base ** expoente

print(f"2^3 = {potencia(2)}")
print(f"2^3 = {potencia(2, 3)}")