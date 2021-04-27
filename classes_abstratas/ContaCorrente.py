from ContaBancaria import ContaBancaria


class ContaCorrente(ContaBancaria):
    def __init__(self, valor=0):
        if valor > 0:
            self._valor = valor
        else:
            self._valor = 0

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def depositar(self, novovalor):
        if novovalor >= 0:
            self._valor = novovalor
        else:
            print("Só são permitidos depósitos.")

    def cadastrar(self):
        print("Cadastro processado.")