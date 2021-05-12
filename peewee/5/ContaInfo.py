import abc
from ContaModel import Conta, db
from peewee import *


class ContaInfo(abc.ABC):

    # def __init__(self, numero, agencia, saldo, tipoConta):
    #     conta = Conta.create(numero=numero, agencia=agencia,
    #                          saldo=saldo, tipoConta=tipoConta)
    #     conta.save()

    @abc.abstractmethod
    def mostrarSaldo(self):
        pass
