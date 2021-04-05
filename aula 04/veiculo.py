class veiculo:
    def __init__(self, marca, qtdRodas, modelo, velocidade = 0):
        self.marca = str(marca)
        self.qtdRodas = int(qtdRodas)
        self.modelo = str(modelo)
        self.velocidade = int(velocidade)
    
    def imprimirInformacoes(self):
        print(f"A Marca deste Veículo é {self.marca}, conta com {self.qtdRodas} Rodas, o Modelo é {self.modelo} e alcança a Velocidade de {self.velocidade} km/h.")

    def acelerar(self, valor):
        aceleracao = self.velocidade + valor
        print(f"O Veículo alcança uma Aceleração de {aceleracao} km/h.")
    
    def frear(self, valor):
        parada = self.velocidade - valor     
        print(f"O poder de parada foi de {parada}.")