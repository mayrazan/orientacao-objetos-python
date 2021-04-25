import abc


class Conta(abc.ABC):

    def __init__(self, numero, agencia, saldo, tipoConta):
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo
        self.tipoConta = tipoConta

    @abc.abstractmethod
    def mostrarSaldo(self):
        pass
