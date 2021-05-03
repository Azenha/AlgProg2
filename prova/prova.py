from abc import ABC, abstractmethod


class Computador(ABC):
    @abstractmethod
    def getInformacoes(self, modelo, cor, preco):
        pass

    @abstractmethod
    def cadastrar(self):
        pass


class Desktop(Computador):
    def getInformacoes(self, modelo, cor, preco, _potenciaDaFonte):
        print("\n Modelo:", modelo, "\n Cor:", cor, "\n Preço:", preco,
              "\n Fonte:", _potenciaDaFonte)

    def cadastrar(self):
        print("Cadastro processado.")


class Notebook(Computador):
    def getInformacoes(self, modelo, cor, preco, __tempoDeBateria):
        print("\n Modelo:", modelo, "\n Cor:", cor, "\n Preço:", preco,
              "\n Bateria:", __tempoDeBateria)

    def cadastrar(self):
        print("Cadastro processado.")


a = Desktop()
a.getInformacoes("Dell", "Vostro", "Verde", "650W")
a.cadastrar()

b = Notebook()
b.getInformacoes("Acer", "14 Polegadas", "Preto", "4 Horas")
b.cadastrar()