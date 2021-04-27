class Candidato:

    def __init__(self, nome, partido):
        self.nome = nome
        self.partido = partido

    def __str__(self):
        return "Candidato: {}, {}".format(self.nome, self.partido)
