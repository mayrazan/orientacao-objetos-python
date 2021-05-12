from ContaInfo import ContaInfo
from ContaModel import Conta, ContaImposto, db
from peewee import *


class ContaImpostoInfo(ContaInfo):
    def __init__(self, numero, agencia, saldo, tipoConta, percentualImposto):
        conta = Conta.create(numero=numero, agencia=agencia,
                             saldo=saldo, tipoConta=tipoConta, tipo=2)
        conta.save()
        infoConta = Conta.select(Conta.id).where(
            Conta.tipo == 2).get()
        contaImposto = ContaImposto.create(
            conta=infoConta, percentualImposto=percentualImposto)
        contaImposto.save()

    def calcularImposto(self):
        conta = ContaImposto.select(ContaImposto.percentualImposto).join(Conta).where(
            ContaImposto.conta_id == Conta.id).get()

        for info in Conta.select():
            if(info.tipo == 2):
                info.saldo = info.saldo - \
                    (info.saldo * conta.percentualImposto)
                info.save()
                return info.saldo

    def mostrarSaldo(self):
        query = (Conta
                 .select(Conta.saldo)
                 .join(ContaImposto)
                 .where(Conta.id == ContaImposto.conta_id))
        for info in query:
            print("Saldo conta imposto: ", info.saldo)
