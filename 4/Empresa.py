class Empresa:

    def __init__(self, nome, funcionario):
        self.nome = nome
        self.funcionario = funcionario

    def __str__(self):
        return "Empresa = {}, funcionario = {}".format(self.nome, self.funcionario)
