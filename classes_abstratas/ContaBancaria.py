from abc import ABC, abstractmethod


class ContaBancaria(ABC):
    @property
    def valor(self):
        pass

    @valor.setter
    @abstractmethod
    def cadastrar(self):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass