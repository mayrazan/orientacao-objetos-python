from PessoasModel import PessoasModel, db
from peewee import *


class Pessoas:

    def envelhecer(self):
        for idadePessoa in PessoasModel.select():
            idadePessoa.idade += 1
            idadePessoa.save()

    def engordar(self):
        for pesoPessoa in PessoasModel.select():
            pesoPessoa.peso += 1
            pesoPessoa.save()

    def emagrecer(self):
        for pesoPessoa in PessoasModel.select():
            pesoPessoa.peso -= 1
            pesoPessoa.save()

    def crescer(self):
        for alturaPessoa in PessoasModel.select():
            if(alturaPessoa.idade < 21):
                alturaPessoa.altura += 0.5
            else:
                alturaPessoa.altura += 1
            alturaPessoa.save()

    def imprime(self):
        query = (PessoasModel
                 .select(PessoasModel.nome, PessoasModel.idade, PessoasModel.peso, PessoasModel.altura))
        for pessoa in query:
            print(pessoa.nome, pessoa.idade, pessoa.peso, pessoa.altura)


pessoa = PessoasModel.create(nome="Mayra", idade=19, peso=50, altura=160)
pessoa.save()
p = Pessoas()
p.imprime()
p.crescer()
p.emagrecer()
p.imprime()
p.engordar()
p.envelhecer()
p.imprime()
