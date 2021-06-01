from Pilha import Pilha


pilha = Pilha()
pilha.espiar()
pilha.remover()
pilha.empilhar("A")
pilha.empilhar("B")
pilha.empilhar("C")
pilha.remover()
pilha.empilhar("D")
pilha.empilhar("E")
print(pilha)
print(len(pilha))
print(pilha.espiar())