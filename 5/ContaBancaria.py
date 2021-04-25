from Conta import Conta


class ContaBancaria(Conta):

    def __init__(self, numero, agencia, saldo, tipoConta):
        Conta.__init__(self, numero, agencia, saldo, tipoConta)

    def mostrarSaldo(self):
        print("Saldo conta bancaria: ", self.saldo)

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")
