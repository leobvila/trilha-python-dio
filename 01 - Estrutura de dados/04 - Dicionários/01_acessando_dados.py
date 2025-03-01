dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

#acessando o Valor 
print(dados["nome"])  # "Guilherme"
print(dados["idade"])  # 28
print(dados["telefone"])  # "3333-1234"

#alterando o valor 
dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

#acessando o dicionario
print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}
