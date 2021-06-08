pessoa = { "nome" : "Júlia" , "idade" : 68 }

print( pessoa )


print( pessoa["nome"] )


pessoa["nome"] = "Iracema"


print( pessoa )


pessoa["altura"] = 1.75


print( pessoa )


del pessoa["idade"]

print("########")


print( pessoa )


print( "--------------------------" )


pessoa2 = { "nome": "Júlia" , "vacinada" : False }

pessoa3 = { "nome": "Iracema" , "vacinada" : True } 


pessoas = pessoa2, pessoa3 


print( pessoas )