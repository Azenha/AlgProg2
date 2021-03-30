class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def printAluno(self):
        print("\nAluno \nCódigo:", self.codigo, "\nNome:", self.nome, "\nMatrícula:", self.matricula)


class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        super().__init__(codigo, nome, matricula)
        self.ano = ano

    def printAlunoEnsinoMedio(self):
        print("\nAluno Ensino Médio \nCódigo:", self.codigo, "\nNome:",  self.nome, "\nMatrícula:",  self.matricula, "\nAno:", self.ano)


class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        super().__init__(codigo, nome, matricula)
        self.semestre = semestre

    def printAlunoGraduacao(self):
        print("\nAluno Graduação \nCódigo:", self.codigo, "\nNome:",  self.nome, "\nMatrícula:",  self.matricula, "\nSemestre:", self.semestre)


generico = Aluno("001", "Leonardo", "000001")
generico.printAluno()

medio = AlunoEnsinoMedio("002", "Azenha", "000002", "2000")
medio.printAlunoEnsinoMedio()

graduacao = AlunoGraduacao("003", "Silva", "000003", "Terceiro")
graduacao.printAlunoGraduacao()