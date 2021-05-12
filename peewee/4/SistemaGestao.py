from Gestao import Pessoa, Empresa, Funcionario, db
from peewee import *

pessoa = Pessoa.create(nome="Mayra", endereco="Endereço",
                       telefone="123456", cpf="456789-99")
pessoa.save()

infoPessoa = Pessoa.select(Pessoa.id).get()

funcionario = Funcionario.create(pessoa=infoPessoa, salario=2000)
funcionario.save()

infoFuncionario = Funcionario.select(Funcionario.id).get()

empresa = Empresa.create(nome="Empresa", funcionario=infoFuncionario)
empresa.save()

query = (Pessoa
         .select(Pessoa.nome, Pessoa.endereco, Pessoa.telefone, Pessoa.cpf, Funcionario.salario, Empresa.nome)
         .join(Funcionario)
         .join(Empresa)
         .where((Pessoa.id == Funcionario.pessoa_id) & (Empresa.funcionario_id == Funcionario.id)))

for info in query:
    print(info.nome, info.endereco, info.telefone, info.cpf,
          info.funcionario.salario, info.funcionario.empresa.nome)
