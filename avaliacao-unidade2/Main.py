from UrnaEletronica import UrnaEletronica
from Voto import Voto
import sys
from datetime import datetime
from Eleitor import Eleitor
from Candidato import Candidato


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
            eleitor = Eleitor(nomeEleitor, tituloEleitor)

            print("-------------Selecione um candidato-------------------")
            print("0. Pedro ")
            print("1. João ")
            print("2. Mauro ")
            numero = int(
                input("Digite o número correspondente acima para selecionar o candidato: "))

            if(numero > 2):
                print("Número não existe")
            else:
                candidato = urna.candidatos[numero]
                votos = Voto(datetime.now(), candidato, eleitor)
                urna.adicionarVoto(votos)
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

            numero = int(
                input("Digite o número do partido para selecionar o candidato: "))
            print("------------------------------------------------------")
            urna.listarVoto(numero)
            print("------------------------------------------------------")
            self.menu()
        while opcao == "0":
            sys.exit()
        if opcao > "4" or opcao < "0":
            print("Opção inválida.")


urna = UrnaEletronica()
m = Main()
m.menu()
