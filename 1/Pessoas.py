class Pessoas:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1

    def engordar(self):
        self.peso += 1

    def emagrecer(self):
        self.peso -= 1

    def crescer(self):
        if(self.idade < 21):
            self.altura += 0.5
        else:
            self.altura += 1

    def imprime(self):
        print(self.nome, self.idade, self.peso, self.altura)


pessoa = Pessoas("Mayra", 19, 50, 160)

pessoa.imprime()
pessoa.crescer()
pessoa.emagrecer()
pessoa.imprime()
pessoa.engordar()
pessoa.envelhecer()
pessoa.imprime()
