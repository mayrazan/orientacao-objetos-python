class Empregado:

    def __init__(self, nome, sobrenome, salarioMensal):
        self._nome = nome
        self._sobrenome = sobrenome
        self._salarioMensal = salarioMensal
        self.aumentoSalario = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome

    @property
    def salarioMensal(self):
        return self._salarioMensal

    @salarioMensal.setter
    def salarioMensal(self, salarioMensal):
        if(self._salarioMensal < 0):
            self._salarioMensal = 0
        else:
            self._salarioMensal = salarioMensal

    def aumento(self):
        self.aumentoSalario = self._salarioMensal * 0.1
        self._salarioMensal += self.aumentoSalario

    def salarioAnual(self):
        return self._salarioMensal * 12
