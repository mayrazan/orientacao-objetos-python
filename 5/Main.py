from ContaImposto import ContaImposto
from ContaBancaria import ContaBancaria

contaImposto = ContaImposto("1234-5", "1234-3", 2000, "corrente", 0.4)
contaBancaria = ContaBancaria("5475-5", "8745-3", 1000, "poupanca")

contaImposto.mostrarSaldo()
print(contaImposto.calcularImposto())
contaBancaria.sacar(50)
contaBancaria.mostrarSaldo()
contaBancaria.depositar(100)
contaBancaria.mostrarSaldo()
