class BombaCombustivel:

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valorAbastecido):
        quantidade = valorAbastecido / self.valorLitro
        print("Quantidade de litros: ", quantidade)
        self.quantidadeCombustivel -= quantidade
        return quantidade

    def abastecerPorLitro(self, quantidadeLitros):
        valorFinal = quantidadeLitros * self.valorLitro
        print("Valor a ser pago: ", valorFinal)
        self.quantidadeCombustivel -= quantidadeLitros
        return valorFinal

    def alterarValor(self, novoValor):
        self.valorLitro = novoValor
        return self.valorLitro

    def alterarCombustivel(self, novoTipo):
        self.tipoCombustivel = novoTipo
        return self.tipoCombustivel

    def alterarQuantidadeCombustivel(self, novaQuantidade):
        self.quantidadeCombustivel += novaQuantidade
        return self.quantidadeCombustivel

    def imprime(self):
        print(self.tipoCombustivel, self.valorLitro, self.quantidadeCombustivel)


bomba = BombaCombustivel("comum", 3, 300)

bomba.abastecerPorValor(50)
bomba.abastecerPorLitro(20)
bomba.imprime()
bomba.alterarValor(4)
bomba.abastecerPorValor(50)
bomba.abastecerPorLitro(20)
bomba.alterarCombustivel("aditivada")
bomba.imprime()
bomba.alterarQuantidadeCombustivel(50)
bomba.imprime()
