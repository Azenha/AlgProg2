carros = "Mille", "Chevett", "Doblo", 25, 3.7, True

print(carros)

# carros[1] = "Toro"

print(carros[2])

print("--------------------------")

for car in carros:

    print(car)

#pegando um intervalo na tupla

print(carros[1:4])

print(carros[2:])

print(carros[-2])

print(carros[-4:])

carros = "Mille", "Chevett", "Doblo"

print(sorted(carros))

print(carros)

novaLista = sorted(carros)

novaLista[1] = "Doblo Adventure"

print(novaLista)

for cont in range(len(carros)):

    print("Posição ", cont, " - Carro: ", carros[cont])

print("____----------_____")

for index, car in enumerate(carros):

    print("Posição ", index, " - Carro: ", car)

#def calcular( x , y ) :

#  valores = (x+y) , (x-y) , (x*y) , (x/y)

#  return valores


def calcular(x, y):

    return (x + y), (x - y), (x * y), (x / y)


print("------ Usando tuplas em funções -----")

print(calcular(8, 2))
