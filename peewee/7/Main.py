from peewee import *
from Empregado import Empregado

empregado1 = Empregado("Mayra", "Souza", 3000)
empregado2 = Empregado("Pedro", "Ribeiro", 2000)

print("empregado 1")
empregado1.mostrar(1)
empregado1.salarioAnual(1)
empregado1.mostrar(1)

print("empregado 2")
empregado2.mostrar(2)
empregado2.salarioAnual(2)
empregado2.mostrar(2)


print("empregado 1 - aumento")
empregado1.aumento(1)
empregado1.mostrar(1)
empregado1.salarioAnual(1)
empregado1.mostrar(1)

print("empregado 2 - aumento")
empregado2.aumento(2)
empregado2.mostrar(2)
empregado2.salarioAnual(2)
empregado2.mostrar(2)
