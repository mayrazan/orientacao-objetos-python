from Candidato import Candidato
from Partido import Partido


class UrnaEletronica:

    def __init__(self):
        self.candidatos = []
        self.votos = []
        self.secao = 0
        self.zona = 0

    def inicializar(self):
        partido1 = Partido(51, "psd")
        partido2 = Partido(15, "mdb")
        partido3 = Partido(11, "pp")
        candidato1 = Candidato("Pedro", partido1)
        candidato2 = Candidato("João", partido2)
        candidato3 = Candidato("Mauro", partido3)
        self.candidatos.append(candidato1)
        self.candidatos.append(candidato2)
        self.candidatos.append(candidato3)
        self.secao = 123
        self.zona = 456

    def adicionarVoto(self, voto):
        self.votos.append(voto)

    def listarTodosOsVotos(self):
        for i, voto in enumerate(self.votos):
            print("Data: ", voto.data, " - ", voto.candidato)

    def listarVoto(self, candidato):
        cont = 0
        for i, infoCandidato in enumerate(self.votos):
            if(infoCandidato.candidato.partido.numero == candidato):
                cont += 1
                print("Hora de cada voto: ", infoCandidato.data)
        print("Número total de votos: ", cont)

    def __str__(self):
        return "Candidato: {}, Votos: {}, Seção: {}, Zona: {}".format(self.candidatos, self.votos, self.secao, self.zona)
