from model.Pessoa import Pessoa


class Fisica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso,
                 altura):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cpf = str(cpf)
        self.idade = int(idade)
        self.peso = float(peso)
        self.altura = float(altura)

    def imprimeCPF(self):
        print(f"Cadastro de Pessoa Física {self.__cpf}.")

    def __calculaIMC(self):
        print(f"Índice de Massa Corporal {((self.peso)/(self.altura)**2)}.")
