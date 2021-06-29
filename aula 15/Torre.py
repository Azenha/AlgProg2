class Torre:
    def __init__(self):
        self.id = int()
        self.nome = str()
        self.endereco = str()

    def cadastrar(self):
        self.id = int(input("Digite o ID da Torre: "))
        self.nome = str(input("Digite o Nome da Torre: "))
        self.endereco = str(input("Digite o Endereço da Torre: "))
    
    def imprimir(self):
        print(f"A id da Torre é {self.id} e o nome é {self.nome} localizada no endereço {self.endereco}")