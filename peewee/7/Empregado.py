from EmpregadoModel import EmpregadoInfo, db
from peewee import *


class Empregado:

    def __init__(self, nome, sobrenome, salarioMensal):
        empregado = EmpregadoInfo.create(nome=nome, sobrenome=sobrenome,
                                         salarioMensal=salarioMensal, aumentoSalario=0)
        empregado.save()

    @property
    def nome(self):
        nome = EmpregadoInfo.select(EmpregadoInfo.nome).get()
        return nome

    @nome.setter
    def nome(self, nome):
        for nomeEmpregado in EmpregadoInfo.select():
            nomeEmpregado.nome = nome
            nomeEmpregado.save()

    @property
    def sobrenome(self):
        sobrenome = EmpregadoInfo.select(EmpregadoInfo.sobrenome).get()
        return sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        for sobrenomeEmpregado in EmpregadoInfo.select():
            sobrenomeEmpregado.sobrenome = sobrenome
            sobrenomeEmpregado.save()

    @property
    def salarioMensal(self):
        salario = EmpregadoInfo.select(EmpregadoInfo.salarioMensal).get()
        return salario

    @salarioMensal.setter
    def salarioMensal(self, salarioMensal):
        for salario in EmpregadoInfo.select():
            if(salario.salarioMensal < 0):
                salario.salarioMensal = 0
                salario.save()
            else:
                salario.salarioMensal = salarioMensal
                salario.save()

    def aumento(self, id):
        for aumento in EmpregadoInfo.select():
            if(aumento.id == id):
                aumento.aumentoSalario = aumento.salarioMensal * 0.1
                aumento.salarioMensal += aumento.aumentoSalario
                aumento.save()

    def salarioAnual(self, id):
        for salario in EmpregadoInfo.select():
            if(salario.id == id):
                salario.salarioMensal = salario.salarioMensal * 12
                salario.save()
                return salario.salarioMensal

    def mostrar(self, id):
        query = (EmpregadoInfo.select(EmpregadoInfo.nome, EmpregadoInfo.sobrenome,
                                      EmpregadoInfo.salarioMensal, EmpregadoInfo.aumentoSalario).where(EmpregadoInfo.id == id))
        for info in query:
            print(info.nome, info.sobrenome,
                  info.salarioMensal, info.aumentoSalario)
