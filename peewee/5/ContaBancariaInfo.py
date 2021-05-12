from ContaInfo import ContaInfo
from ContaModel import Conta, ContaBancaria, db
from peewee import *


class ContaBancariaInfo(ContaInfo):

    def __init__(self, numero, agencia, saldo, tipoConta):
        conta = Conta.create(numero=numero, agencia=agencia,
                             saldo=saldo, tipoConta=tipoConta, tipo=1)
        conta.save()
        # conta = Conta.__init__(self, numero, agencia, saldo, tipoConta)
        infoConta = Conta.select(Conta.id).where(
            Conta.tipo == 1).get()
        contaBancaria = ContaBancaria.create(conta=infoConta)
        contaBancaria.save()

    def mostrarSaldo(self):
        query = (Conta
                 .select(Conta.saldo)
                 .join(ContaBancaria)
                 .where(Conta.id == ContaBancaria.conta_id))
        for info in query:
            print("Saldo conta bancaria: ", info.saldo)

    def depositar(self, valor):
        for info in Conta.select():
            if(info.tipo == 1):
                info.saldo += valor
                info.save()

    def sacar(self, valor):
        for info in Conta.select():
            if(info.tipo == 1):
                if (info.saldo >= valor):
                    info.saldo -= valor
                    info.save()
                else:
                    print("Saldo insuficiente!")
