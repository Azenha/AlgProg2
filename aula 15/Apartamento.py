class Apartamento:
    def __init__(self):
        self.id = int()
        self.numero = str()
        self.torre = None
        # self.vaga = int()
        # self.proximo = None

    def cadastrar(self,valor):
        self.id = int(input("Digite o ID do Apartamento: "))
        self.numero = str(input("Digite o Número do Apartamento: "))
        self.torre = valor
    
    def imprimir(self):
        print(f"O id do Apartamento é {self.id} no número {self.numero} localizado na Torre {self.torre.nome}")