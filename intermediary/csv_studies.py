import csv

# Escrever CSV
dados = [
    ["Nome", "Idade", "Cidade"],
    ["João", "30", "São Paulo"],
    ["Maria", "32", "Rio de Janeiro"],
    ["Yuri", "32", "Curitiba"],
]

with open("pessoas.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)

# Ler CSV
with open("pessoas.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)