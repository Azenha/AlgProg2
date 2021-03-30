produto = ["maçã","laranja","banana","melão","morango","manga"]
valores = ["6,90","3,90","2,90","4,90","9,90","5,90"]
estoque = ["10","15","25","5","5","10"]

def listar(num):
    print(f"Você escolheu {produto[num]}, que custa R$ {valores[num]} e tem um estoque de {estoque[num]} unidades.\n")

def remover(num):
    produto.pop(num)
    valores.pop(num)
    estoque.pop(num)

while True:
    x = 0
    for y in produto:
        print(x,"-", y)
        x+=1
    print("Ver detalhes de um produto ou remover um produto da lista?")
    opcao = int(input("Digite 0 para detalhes ou 1 para excluir: "))
    escolha = int(input("Digite o nº do produto: "))
    if opcao == 0:
        listar(escolha)
    elif opcao == 1:
        remover(escolha)
        print(f"Produto {produto[escolha]} Removido com Sucesso!\n")
    sair = input("Para sair do programa digite SAIR: ").upper()
    if sair == "SAIR" :
        break