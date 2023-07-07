class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.saques_realizados = 0

    def deposito(self, valor):
        self.saldo += valor
        print(
            f"Depósito de R$ {valor} realizado. Saldo atual: R$ {self.saldo}")

    def saque(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser maior que zero.")
        elif valor > 500:
            print("O valor do saque excede o limite de R$ 500.")
        elif self.saques_realizados >= 3:
            print("Você já realizou o limite máximo de saques para hoje.")
        elif self.saldo < valor:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.saques_realizados += 1
            print(
                f"Saque de R$ {valor} realizado. Saldo atual: R$ {self.saldo}")

    def extrato(self):
        print(f"Saldo: R$ {self.saldo}")
        print(f"Saques realizados hoje: {self.saques_realizados}")


sistema = SistemaBancario()

while True:
    print("\n1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        sistema.deposito(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        sistema.saque(valor)
    elif opcao == "3":
        sistema.extrato()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")
