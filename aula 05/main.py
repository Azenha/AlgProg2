from model.Pessoa import Pessoa
from model.Fisica import Fisica
from model.Juridica import Juridica

print("-=-= Pessoa =-=-")
leonardo = Pessoa(123, "Leonardo", "José do Patrocínio", "(51)9XXXX-4321")
leonardo.imprimeNome()

print("-=-= Pessoa Fisica =-=-")
azenha = Fisica(456, "Azenha", "Demétrio Ribeiro", "(51)9XXXX-1234",
                     "XXX.123.456-XX", "34", 98.0, 1.77)
azenha.imprimeCPF()

print("-=-= Pessoa Juridica =-=-")
silva = Juridica(789, "Silva", "Borges de Medeiros", "(51)95678-1234",
                         "XX.XXX.XXX/0001-XX", "XX.XXXXXX-1", 13)
silva.imprimeCNPJ()

print("-=-= Métodos fortemente privados \"__\" não são executados. =-=-")