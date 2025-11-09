class ContaBancaria:
    def __init__(self, titular, saldo_inicial = 0):
        self.titular = titular
        self.__saldo = saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso"
        return "Valor inválido"
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso"
        return "Saldo insuficiente ou valor inválido"
    
    def get_saldo(self):
        return f"Saldo atual: R${self.__saldo:.2f}"
    
# Usar a classe

conta = ContaBancaria("Yuri", 1000)
print(conta.get_saldo())
print(conta.depositar(500))
print(conta.sacar(200))
print(conta.get_saldo())