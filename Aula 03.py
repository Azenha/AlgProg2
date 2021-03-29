class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def printAluno(self):
        print(self.codigo, self.nome, self.matricula)


class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        super().__init__(codigo, nome, matricula)
        self.ano = ano

    def printAlunoEnsinoMedio(self):
        print(self.codigo, self.nome, self.matricula, self.ano)


class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        super().__init__(codigo, nome, matricula)
        self.semestre = semestre

    def printAlunoGraduacao(self):
        print(self.codigo, self.nome, self.matricula, self.semestre)


generico = Aluno("001", "Leonardo", "000001")
generico.printAluno()

medio = AlunoEnsinoMedio("002", "Azenha", "000002", "2000")
medio.printAlunoEnsinoMedio()

graduacao = AlunoGraduacao("003", "Silva", "000003", "Terceiro")
graduacao.printAlunoGraduacao()