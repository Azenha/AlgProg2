from ContaBancaria import ContaBancaria
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca


a = ContaCorrente()
a.cadastrar()
a.depositar = -10
print( a.depositar)

a = ContaPoupanca()
a.cadastrar()
a.depositar = 50
print( a.depositar)
