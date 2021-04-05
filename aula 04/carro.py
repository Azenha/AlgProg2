from automovel import automovel

class carro(automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, qtdPortas, velocidade = 0):
        automovel.__init__(self, marca, qtdRodas, modelo, potenciaDoMotor, velocidade)
        self.qtdPortas = int(qtdPortas)

    def imprimirInformacoes(self):
        automovel.imprimirInformacoes(self)
        print(f"Este carro possui {self.qtdPortas} portas.")