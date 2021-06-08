def Media(nota1, nota2):
    mediaCalculada = (nota1 + nota2) / 2
    return mediaCalculada


notas = {}

nomeAluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota 1 do aluno: "))
nota2 = float(input("Digite a nota 2 do aluno: "))

notas = dict({"nome": nomeAluno, "nota1": nota1, "nota2": nota2})

print(notas)

mediaAluno = Media(nota1, nota2)

notas["media"] = mediaAluno

print(notas)