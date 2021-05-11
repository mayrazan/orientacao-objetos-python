from UrnaEletronica import UrnaEletronica
import sys
from datetime import datetime
from Model import Candidato, Eleitor, Partido, Voto, db
from peewee import *


class Main:

    def menu(self):
        print("Selecione uma opção: ")
        print("1. Inicializar: ")
        print("2. Adicionar Voto: ")
        print("3. Listar todos os votos: ")
        print("4. Listar voto: ")
        print("0. Sair. ")
        opcao = input("> ")

        while opcao == "1":
            urna.inicializar()
            print("Votação iniciada")
            print("------------------------------------------------------")
            self.menu()
        while opcao == "2":
            nomeEleitor = input("Digite seu nome: ")
            tituloEleitor = input("Digite seu titulo de eleitor: ")
            dadosEleitor = Eleitor.create(
                nome=nomeEleitor, tituloEleitor=tituloEleitor)
            dadosEleitor.save()

            print("-------------Selecione um candidato-------------------")
            print("1. Pedro ")
            print("2. João ")
            print("3. Mauro ")
            numero = int(
                input("Digite o número correspondente acima para selecionar o candidato: "))

            if(numero > 3):
                print("Número não existe")
            else:
                candidato = Candidato.select(Candidato.id).where(
                    Candidato.id == numero).get()
                eleitor = Eleitor.select(Eleitor.id).where(
                    Eleitor.nome == nomeEleitor).get()
                urna.adicionarVoto(data=datetime.now(),
                                   candidato=candidato, eleitor=eleitor)
                print("Voto computado com sucesso!")
                print("------------------------------------------------------")
            self.menu()
        while opcao == "3":
            urna.listarTodosOsVotos()
            print("------------------------------------------------------")
            self.menu()
        while opcao == "4":
            print("-------------Selecione um candidato-------------------")
            print("51. Pedro ")
            print("15. João ")
            print("11. Mauro ")

            numero = input(
                "Digite o número do partido para selecionar o candidato: ")
            print("------------------------------------------------------")
            urna.listarVoto(numero)
            print("------------------------------------------------------")
            self.menu()
        while opcao == "0":
            sys.exit()
            db.close()
        if opcao > "4" or opcao < "0":
            print("Opção inválida.")


urna = UrnaEletronica()
m = Main()
m.menu()
