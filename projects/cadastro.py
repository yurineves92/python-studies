class SistemaCadastro:
    def __init__(self):
        self.usuarios = {}
    
    def cadastrar(self, nome, email, idade):
        if email in self.usuarios:
            return "Email já cadastrado!"

        self.usuarios[email] = {
            "nome": nome,
            "idade": idade
        }

        return "Usuário cadastrado com sucesso!"
    
    def buscar(self, email):
        if email in self.usuarios:
            return self.usuarios[email]
        return "Usuário não encontrado!"
    
    def listar_todos(self):
        if not self.usuarios:
            return "Nenhum usuário cadastrado"

        resultado = "=== USUÁRIOS CADASTRADOS ===\n"
        for email, dados in self.usuarios.items():
            resultado += f"Nome:{dados['nome']}, Email: {email}, Idade: {dados['idade']}\n"
        return resultado
    
    def remover(self, email):
        if email in self.usuarios:
            del self.usuarios[email]
            return "Usuário removido com sucesso!"
        return "Usuário não encontrado"
    
# Usar o sistema
sistema = SistemaCadastro()

while True:
    print("\n=== SISTEMA DE CADASTRO ===")
    print("1. Cadastro usuário")
    print("2. Buscar usuário")
    print("3. Listar todos")
    print("4. Remover usuário")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        idade = int(input("Idade: "))
        print(sistema.cadastrar(nome, email, idade))
    
    elif opcao == "2":
        email = input("Email: ")
        print(sistema.buscar(email))

    elif opcao == "3":
        print(sistema.listar_todos())

    elif opcao == "4":
        email = input("Email: ")
        print(sistema.remover(email))

    elif opcao == "5":
        print("Até logo")
        break

    else:
        print("Opção inválida")