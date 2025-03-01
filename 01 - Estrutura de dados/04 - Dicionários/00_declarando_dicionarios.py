#Dicionario é um conjunto  não-ordenado de pares chave:valor, onde chaves sao unicas emuma dada instancia do dicionario. Dicionario são delimetados por chaves: {}, e contem uma lista de pares chave:valor separados por virgula , ex: nome = {"nome": "Leonardo", "sobrnome": "Vila"}
# para um dicionario a chave tem q ser imutavel o valor pode ser mutavel ou imutavel
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

# adicionando uma nova chave ex: pessoa["telefone"]= "o valor" 
pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)
