from No import No


class Dupla:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
        self.fim = None

    def adicionar(self, valor):
        if self.inicio:
            cursor = self.inicio
            while cursor.proximo:
                cursor = cursor.proximo
            cursor.proximo = No(valor, cursor)
            self.fim = cursor.proximo
        else:
            self.inicio = No(valor, None)
            self.fim = self.inicio
        self.tamanho += 1

    def imprimir(self):
        # if self.tamanho == 0 :
        if self.inicio == None :
            print("Lista vazia!")
        else:
            aux = self.inicio
            while(aux): #(aux != None): 
                print(aux.dado)
                aux = aux.proximo
            print("Tamanho da lista: ", self.tamanho)

    def reverso(self):
        if self.fim == None:
            print("Lista vazia")
        else:
            aux = self.fim
            while aux:
                print(aux.dado)
                aux = aux.anterior
            print("Tamanho da lista: ", self.tamanho)
