"""
Implementar uma pilha de objetos Livro.
O objeto Livro também deve possuir os atributos id, título e autor.
O atributo autor será utilizado para armazenar um objeto do tipo Autor.
A classe Autor deve possuir o atributo fortemente privado id e o atributo público nome.
O sistema deverá possuir métodos para inserir e para retirar livros da pilha.
"""


class Autor:
    __id = str()

    def __init__(self, id, nome):
        self.__id = id
        self.nome = str(nome)

    def imprimir(self):
        print("ID:", self.__id)
        print("Nome:", self.nome)


class Livro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor


class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def empilhar(self, titulo):
        no = No(titulo)
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
        print("Não há livros na pilha!")


autor1Id = input("Digite a ID do Autor 1: ")
autor1Nome = input("Digite o Nome do Autor 1: ")
autor1 = Autor(autor1Id, autor1Nome)
autor1.imprimir()

autor2 = Autor("2", "Azenha")
autor3 = Autor("3", "Da")
autor4 = Autor("4", "Silva")
autor2.imprimir()
autor3.imprimir()
autor4.imprimir()

livro1Id = input("Digite a ID do Autor 1: ")
livro1Titulo = input("Digite o título do livro 1: ")
livro1Autor = autor1.nome
livro1 = Livro(livro1Id, livro1Titulo, livro1Autor)

livro2 = Livro("2", "foo", autor2.nome)
livro3 = Livro("3", "bar", autor3.nome)
livro4 = Livro("4", "foobar", autor4.nome)

print(f"{livro1.id} - {livro1.titulo} - {livro1.autor}")
print(f"{livro2.id} - {livro2.titulo} - {livro2.autor}")
print(f"{livro3.id} - {livro3.titulo} - {livro3.autor}")
print(f"{livro4.id} - {livro4.titulo} - {livro4.autor}")

pilha = Pilha()
pilha.empilhar(livro1.titulo)
pilha.empilhar(livro2.titulo)
pilha.empilhar(livro3.titulo)
print(pilha)
pilha.remover()
pilha.empilhar(livro4.titulo)
print(pilha)
pilha.remover()
pilha.remover()
pilha.remover()
pilha.remover()
pilha.remover()
