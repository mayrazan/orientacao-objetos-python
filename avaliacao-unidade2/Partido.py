class Partido:

    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome

    def __str__(self):
        return "Numero do partido: {}, Partido: {}".format(self.numero, self.nome)
