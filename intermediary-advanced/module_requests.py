import requests

# Fazer requisição GET
response = requests.get('https://api.github.com')
print(f"Status: {response.status_code}")
print(f"JSON: {response.json()}")

# Requisição com parâmetros
params = {"q": "php"}
response = requests.get('https://api.github.com/search/repositories', params = params)
dados = response.json()
print(f"Total de repositórios: {dados['total_count']}")