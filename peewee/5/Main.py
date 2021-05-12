from ContaModel import Conta, ContaImposto, ContaBancaria, db
from ContaBancariaInfo import ContaBancariaInfo
from ContaImpostoInfo import ContaImpostoInfo
from peewee import *

contaImposto = ContaImpostoInfo("1234-5", "1234-3", 2000, "corrente", 0.4)
contaBancaria = ContaBancariaInfo("5475-5", "8745-3", 1000, "poupanca")

contaImposto.mostrarSaldo()
print("Imposto: ", contaImposto.calcularImposto())
contaBancaria.sacar(50)
contaBancaria.mostrarSaldo()
contaBancaria.depositar(100)
contaBancaria.mostrarSaldo()
