from Conta import Conta


class ContaImposto(Conta):
    def __init__(self, numero, agencia, saldo, tipoConta, percentualImposto):
        Conta.__init__(self, numero, agencia, saldo, tipoConta)
        self.percentualImposto = percentualImposto

    def calcularImposto(self):
        return self.saldo - (self.saldo * self.percentualImposto)

    def mostrarSaldo(self):
        print("Saldo conta imposto: ", self.saldo)
