# Escrever em arquivo
with open("exemplo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")
    arquivo.write("Terceira linha\n")

# Ler arquivo completo
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Ler linha por linha
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())

# Adicionar ao arquivo
with open("exemplo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Quarta linha\n")