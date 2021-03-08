def EhPar(num):
    if num%2 == 0:
        return "par."
    return "ímpar."

num = int(input("Digite um número: "))
tipo = EhPar(num)
print("O número é",tipo)