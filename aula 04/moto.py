from automovel import automovel

class moto(automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, partidaEletrica, velocidade = 0):
        automovel.__init__(self, marca, qtdRodas, modelo, potenciaDoMotor, velocidade)
        self.partidaEletrica = bool(partidaEletrica)

    def imprimirInformacoes(self):
        automovel.imprimirInformacoes(self)
        if self.partidaEletrica == True:
            print(f"Esta Moto possui partida elétrica.")
        else:
            print(f"Esta Moto não possui partida elétrica.")