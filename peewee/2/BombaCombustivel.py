from Bomba import Bomba, db
from peewee import *


class BombaCombustivel:

    def __init__(self):
        bomba = Bomba.create(
            tipoCombustivel="comum", valorLitro=3, quantidadeCombustivel=300)
        bomba.save()

    def abastecerPorValor(self, valorAbastecido):
        for abastecer in Bomba.select():
            quantidade = valorAbastecido / abastecer.valorLitro
            print("Quantidade de litros: ", quantidade)
            abastecer.quantidadeCombustivel -= quantidade
            abastecer.save()
            return quantidade

    def abastecerPorLitro(self, quantidadeLitros):
        for valor in Bomba.select():
            valorFinal = quantidadeLitros * valor.valorLitro
            print("Valor a ser pago: ", valorFinal)
            valor.quantidadeCombustivel -= quantidadeLitros
            valor.save()
            return valorFinal

    def alterarValor(self, novoValor):
        for alterar in Bomba.select():
            alterar.valorLitro = novoValor
            alterar.save()
            return alterar.valorLitro

    def alterarCombustivel(self, novoTipo):
        for alterar in Bomba.select():
            alterar.tipoCombustivel = novoTipo
            alterar.save()
            return alterar.tipoCombustivel

    def alterarQuantidadeCombustivel(self, novaQuantidade):
        for alterar in Bomba.select():
            alterar.quantidadeCombustivel += novaQuantidade
            alterar.save()
            return alterar.quantidadeCombustivel

    def imprime(self):
        query = (Bomba
                 .select(Bomba.tipoCombustivel, Bomba.valorLitro, Bomba.quantidadeCombustivel))
        for bomba in query:
            print(bomba.tipoCombustivel, bomba.valorLitro,
                  bomba.quantidadeCombustivel)


bomba = BombaCombustivel()

bomba.abastecerPorValor(50)
bomba.abastecerPorLitro(20)
bomba.imprime()
bomba.alterarValor(4)
bomba.abastecerPorValor(50)
bomba.abastecerPorLitro(20)
bomba.alterarCombustivel("aditivada")
bomba.imprime()
bomba.alterarQuantidadeCombustivel(50)
bomba.imprime()
