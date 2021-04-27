class Eleitor:

    def __init__(self, nome, tituloEleitor):
        self.nome = nome
        self.tituloEleitor = tituloEleitor

    def __str__(self):
        return "Eleitor: {}, Titulo eleitor: {}".format(self.nome, self.tituloEleitor)
