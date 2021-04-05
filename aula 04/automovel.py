from veiculo import veiculo

class automovel(veiculo):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, velocidade = 0):
        veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.potenciaDoMotor = float(potenciaDoMotor)

    def imprimirInformacoes(self):
        veiculo.imprimirInformacoes(self)
        print(f"A potência do motor deste Automóvel é de {self.potenciaDoMotor} cv.")