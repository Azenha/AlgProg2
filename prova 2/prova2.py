class Autor:
    __id = str()

    def __init__(self, id, nome):
        self.__id = id
        self.nome = str(nome)


class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    """ Exemplo da aula
    def adicionar(self, valor):
		no = No( valor )
		if self.tamanho == 0 :
			self.topo = no
		else: 
			no.proximo = self.topo
			self.topo = no
		self.tamanho +=1
#		if self.tamanho > 0 :
#			no.proximo = self.topo
#		self.topo = no
    """

    def empilhar(self, elemento):
        no = No(elemento)
        no.proximo = self.topo
        self.topo = no
        self.tamanho += 1

    def remover(self):
        if self.tamanho > 0:
            no = self.topo
            self.topo = self.topo.proximo
            self.tamanho -= 1
            return no.dado
        # raise IndexError("A pilha está vazia")
        print("A pilha está vazia")

    """ Exemplo da aula
    def remover(self):
		if self.tamanho == 0:
			print( "Pilha vazia!" )
		elif self.tamanho == 1:
			self.topo = None
			self.tamanho = 0
		else:
			self.topo = self.topo.proximo
			self.tamanho -= 1
		self.imprimir()
    """

    def espiar(self):
        if self.tamanho > 0:
            return self.topo.dado
        # raise IndexError("A pilha está vazia")
        print("A pilha está vazia")

    """ Exemplo da aula
   	def imprimir(self):
		# if self.topo == None:
		if self.tamanho == 0:
			print( "Pilha vazia!" )
		else:
			aux = self.topo
			while( aux ) :
				print( aux.dado )
				aux = aux.proximo
    """

    def __len__(self):
        return self.tamanho

    def __repr__(self):
        r = ""
        ponteiro = self.topo
        while ponteiro:
            r = r + str(ponteiro.dado) + "\n"
            ponteiro = ponteiro.proximo
        return r

    def __str__(self):
        return self.__repr__()
