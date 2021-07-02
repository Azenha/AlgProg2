from Torre import Torre
from Apartamento import Apartamento
from Vagas import Vagas


blocoA = Torre()
blocoA.cadastrar()
blocoA.imprimir()

blocoB = Torre()
blocoB.cadastrar()
blocoB.imprimir()

ap01 = Apartamento()
ap01.cadastrar(blocoA)
ap01.imprimir() 

vaga = Vagas()
vaga.imprimir()
vaga.adicionar("Ap01")
vaga.imprimir()
vaga.adicionar("Ap02")
vaga.imprimir()
vaga.adicionar("Ap03")
vaga.imprimir()
vaga.adicionar("Ap04")
vaga.imprimir()
vaga.adicionar("Ap05")
vaga.imprimir()
vaga.adicionar("Ap06")
vaga.imprimir()

vaga.remover()
vaga.imprimir()
vaga.remover()
vaga.imprimir()
vaga.remover()
vaga.imprimir()
vaga.remover()
vaga.imprimir()
vaga.remover()
vaga.imprimir()
vaga.remover()
vaga.imprimir()