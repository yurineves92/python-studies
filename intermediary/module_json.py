import json

pessoa = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo",
    "hobbies": ["programação", "música", "esportes"]
}

with open("pessoa.json", "w", encoding="utf-8") as arquivo:
    json.dump(pessoa, arquivo, indent=4, ensure_ascii=False)

# Ler JSON
with open("pessoa.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
    print(f"Nome: {dados['nome']}")
    print(f"Hobbies: {', '.join(dados['hobbies'])}")