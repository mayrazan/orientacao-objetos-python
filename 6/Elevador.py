class Elevador:

    def __init__(self, andarAtual=0, capacidade=0, quantidadePessoas=0, totalAndares=0):
        self._andarAtual = andarAtual
        self._capacidade = capacidade
        self._quantidadePessoas = quantidadePessoas
        self._totalAndares = totalAndares

    @property
    def andarAtual(self):
        return self._andarAtual

    @andarAtual.setter
    def andarAtual(self, andarAtual):
        self._andarAtual = andarAtual

    @property
    def capacidade(self):
        return self._capacidade

    @capacidade.setter
    def capacidade(self, capacidade):
        self._capacidade = capacidade

    @property
    def quantidadePessoas(self):
        return self._quantidadePessoas

    @quantidadePessoas.setter
    def quantidadePessoas(self, quantidadePessoas):
        self._quantidadePessoas = quantidadePessoas

    @property
    def totalAndares(self):
        return self._totalAndares

    @totalAndares.setter
    def totalAndares(self, totalAndares):
        self._totalAndares = totalAndares

    def inicializar(self, capacidade, total):
        self.__init__(0, capacidade, 0, total)

    def entrar(self):
        if(self._quantidadePessoas < self._capacidade):
            self._quantidadePessoas += 1
        else:
            print("Elevador cheio")

    def sair(self):
        if(self._quantidadePessoas > 0):
            self._quantidadePessoas -= 1
        else:
            print("Elevador vazio")

    def subir(self):
        if(self._andarAtual < self._totalAndares):
            self._andarAtual += 1
        else:
            print("Ultimo andar")

    def descer(self):
        if(self._andarAtual > 0):
            self._andarAtual -= 1
        else:
            print("Terreo")


elevador = Elevador()
elevador.inicializar(20, 8)
elevador.entrar()
elevador.entrar()
elevador.entrar()
elevador.subir()
elevador.subir()
print(elevador.quantidadePessoas, elevador.capacidade,
      elevador.andarAtual, elevador.totalAndares)
elevador.sair()
elevador.descer()
print(elevador.quantidadePessoas, elevador.capacidade,
      elevador.andarAtual, elevador.totalAndares)
