from model.Pessoa import Pessoa


class Juridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cnpj,
                 inscricaoEstadual, quantidadeFuncionarios):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cnpj = str(cnpj)
        self.__inscricaoEstadual = str(inscricaoEstadual)
        self.quantidadeFuncionarios = int(quantidadeFuncionarios)

    def imprimeCNPJ(self):
        print(f"Cadastro Nacional de Pessoa Jurídica {self.__cnpj}.")

    def __emitirNotaFiscal(self):
        pass