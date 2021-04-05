from veiculo import veiculo

class bicicleta(veiculo):
    def __init__(self, marca, qtdRodas, modelo,  numMarchas, bagageiro, velocidade = 0):
        veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.numMarchas = int(numMarchas)
        self.bagageiro = bool(bagageiro)

    def imprimirInformacoes(self):
        veiculo.imprimirInformacoes(self)
        print(f"Esta bicicleta tem {self.numMarchas} marchas.")
        if self.bagageiro == True:
            print(f"Esta Bicicleta possui um bagageiro.")
        else:
            print(f"Esta Bicicleta não possui um bagageiro.")