from ElevadorModel import ElevadorInfo, db
from peewee import *


class Elevador:

    def __init__(self, andarAtual=0, capacidade=0, quantidadePessoas=0, totalAndares=0):
        elevador = ElevadorInfo.create(andarAtual=andarAtual, capacidade=capacidade,
                                       quantidadePessoas=quantidadePessoas, totalAndares=totalAndares)
        elevador.save()

    @property
    def andarAtual(self):
        andar = ElevadorInfo.select(ElevadorInfo.andarAtual).get()
        return andar

    @andarAtual.setter
    def andarAtual(self, andarAt):
        for andar in ElevadorInfo.select():
            andar.andarAtual = andarAt
            andar.save()

    @property
    def capacidade(self):
        capacidade = ElevadorInfo.select(ElevadorInfo.capacidade).get()
        return capacidade

    @capacidade.setter
    def capacidade(self, capaci):
        for cap in ElevadorInfo.select():
            cap.capacidade = capaci
            cap.save()

    @property
    def quantidadePessoas(self):
        quantidade = ElevadorInfo.select(ElevadorInfo.quantidadePessoas).get()
        return quantidade

    @quantidadePessoas.setter
    def quantidadePessoas(self, quant):
        for quantidade in ElevadorInfo.select():
            quantidade.quantidadePessoas = quant
            quantidade.save()

    @property
    def totalAndares(self):
        total = ElevadorInfo.select(ElevadorInfo.totalAndares).get()
        return total

    @totalAndares.setter
    def totalAndares(self, totAndares):
        for total in ElevadorInfo.select():
            total.totalAndares = totAndares
            total.save()

    def inicializar(self, capacidade, total):
        for info in ElevadorInfo.select():
            info.capacidade = capacidade
            info.totalAndares = total
            info.save()

    def entrar(self):
        for info in ElevadorInfo.select():
            if(info.quantidadePessoas < info.capacidade):
                info.quantidadePessoas += 1
                info.save()
            else:
                print("Elevador cheio")

    def sair(self):
        for info in ElevadorInfo.select():
            if(info.quantidadePessoas > 0):
                info.quantidadePessoas -= 1
                info.save()
            else:
                print("Elevador vazio")

    def subir(self):
        for info in ElevadorInfo.select():
            if(info.andarAtual < info.totalAndares):
                info.andarAtual += 1
                info.save()
            else:
                print("Ultimo andar")

    def descer(self):
        for info in ElevadorInfo.select():
            if(info.andarAtual > 0):
                info.andarAtual -= 1
                info.save()
            else:
                print("Terreo")

    def mostrar(self):
        query = (ElevadorInfo.select(ElevadorInfo.andarAtual, ElevadorInfo.quantidadePessoas,
                                     ElevadorInfo.capacidade, ElevadorInfo.totalAndares))
        for info in query:
            print(info.quantidadePessoas, info.capacidade,
                  info.andarAtual, info.totalAndares)


elevador = Elevador()
elevador.inicializar(20, 8)
elevador.entrar()
elevador.entrar()
elevador.entrar()
elevador.subir()
elevador.subir()
elevador.mostrar()
elevador.sair()
elevador.descer()
elevador.mostrar()
