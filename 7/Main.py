from Empregado import Empregado

empregado1 = Empregado("Mayra", "Souza", 3000)
empregado2 = Empregado("Pedro", "Ribeiro", 2000)

print("empregado 1")
print(empregado1.nome, empregado1.sobrenome, empregado1.salarioMensal)
print(empregado1.nome, empregado1.sobrenome, empregado1.salarioAnual())

print("empregado 2")
print(empregado2.nome, empregado2.sobrenome, empregado2.salarioMensal)
print(empregado2.nome, empregado2.sobrenome, empregado2.salarioAnual())


print("empregado 1 - aumento")
empregado1.aumento()
print(empregado1.nome, empregado1.sobrenome, empregado1.salarioMensal)
print(empregado1.nome, empregado1.sobrenome,
      empregado1.salarioAnual())

print("empregado 2 - aumento")
empregado2.aumento()
print(empregado2.nome, empregado2.sobrenome, empregado2.salarioMensal)
print(empregado2.nome, empregado2.sobrenome, empregado2.salarioAnual())
