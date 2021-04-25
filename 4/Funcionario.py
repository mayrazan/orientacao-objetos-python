from Pessoa import Pessoa


class Funcionario(Pessoa):

    def __init__(self, nome, endereco, telefone, cpf, salario):
        super().__init__(nome, endereco, telefone, cpf)
        self.salario = salario

    def __str__(self):
        return "{}, endereco = {}, telefone = {}, cpf = {}, salario = {}".format(self.nome, self.endereco, self.telefone, self.cpf, self.salario)
