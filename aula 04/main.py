from veiculo import veiculo
from automovel import automovel
from carro import carro
from moto import moto
from bicicleta import bicicleta


print("")
veiculo_teste = veiculo("Fiat", 4, "Uno", 80)
veiculo_teste.imprimirInformacoes()
valor = 30
print(f"Com {valor} km/h na alteração da velocidade: ")
veiculo_teste.acelerar(valor)
veiculo_teste.frear(valor)

print("")
automovel_teste = automovel("Honda", 4, "Fit", 116, 180)
automovel_teste.imprimirInformacoes()

print("")
carro_teste = carro("Volkswagen", 4, "Gol", 120, 4, 180)
carro_teste.imprimirInformacoes()

print("")
moto_teste = moto("Honda", 2, "Shadow 750", 45, True, 140)
moto_teste.imprimirInformacoes()

print("")
bicicleta_teste = bicicleta("Caloi", 2, "Urbam", 21, True, 20)
bicicleta_teste.imprimirInformacoes()

print("")
