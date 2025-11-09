# Try except básico
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: Digite um número válido!")
except ZeroDivisionError:
    print("Erro: não é possível dividor pro zero!")


# Try-except-else-finally
try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado!")
else:
    print("Arquivo lido com sucesso!")
    print(conteudo)
finally:
    print("Operação finalizada")


# Criar exceção customizada
class IdadeInvalidaError(Exception):
    pass

def verificar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError("A idade não pode ser negativa!")
    if idade > 150:
        raise IdadeInvalidaError("A idade não pode ser maior que 150")
    return True

try:
    verificar_idade(32)
except IdadeInvalidaError as e:
    print(f"Erro: {e}")
