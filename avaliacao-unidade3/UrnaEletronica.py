from Model import Candidato, Eleitor, Partido, Voto, db
from peewee import fn
from peewee import *


class UrnaEletronica:

    def inicializar(self):
        partido1 = Partido.create(numero=51, nome="psd")
        partido2 = Partido.create(numero=15, nome="mdb")
        partido3 = Partido.create(numero=11, nome="pp")
        partido1.save()
        partido2.save()
        partido3.save()
        candidato1 = Candidato.create(
            nome="Pedro", partido=partido1, zona="123", secao="456")
        candidato2 = Candidato.create(
            nome="João", partido=partido2, zona="123", secao="456")
        candidato3 = Candidato.create(
            nome="Mauro", partido=partido3, zona="123", secao="456")
        candidato1.save()
        candidato2.save()
        candidato3.save()

    def adicionarVoto(self, data, candidato, eleitor):
        votos = Voto.create(data=data,
                            candidato=candidato, eleitor=eleitor)
        votos.save()

    def listarTodosOsVotos(self):
        query = (Voto
                 .select(Voto.data, Candidato.nome, Candidato.partido)
                 .join(Candidato)
                 .where(Candidato.id == Voto.candidato_id))

        for voto in query:
            print("Data: ", voto.data, "Candidato: ",
                  voto.candidato.nome, "Número partido: ", voto.candidato.partido.numero, "Partido: ", voto.candidato.partido.nome)

    def listarVoto(self, candidato):
        query = (Voto
                 .select(fn.COUNT(Voto.candidato_id).alias('quantidade_votos'))
                 .join(Candidato)
                 .join(Partido)
                 .where((Candidato.id == Voto.candidato_id) & (Partido.numero == candidato)))

        query2 = (Voto
                  .select(Voto.data, Candidato.nome, Partido.numero)
                  .join(Candidato)
                  .join(Partido)
                  .where((Candidato.id == Voto.candidato_id) & (Partido.numero == candidato)))

        for voto in query:
            print("Número total de votos: ", voto.quantidade_votos)

        for voto in query2:
            print("Hora de cada voto: ", voto.data,
                  "Candidato: ", voto.candidato.nome)
