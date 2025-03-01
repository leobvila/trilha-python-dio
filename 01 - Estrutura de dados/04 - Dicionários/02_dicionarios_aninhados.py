##dicioarios aninhados : dicionarios podem armazenar qualquer tipo de objetos python como valores , desde que aa chave para esse valor seja um objeto imutavel como (strings e numeros).

#varios dicionarios em um mesmo local
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, #dicionario 1 email
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},# dicionario 2 email
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},# dicionario 3 email
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"a": 1}},# dicionario 4 email
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)

extra = contatos["melaine@gmail.com"]
print(extra) #acessa dicionario ex : melaine@...

extra = contatos["melaine@gmail.com"]["extra"]
print(extra) # acesssa do dicionario melaine@....  a chave: valor da chave extra

extra = contatos["melaine@gmail.com"]["extra"]["a"]
print(extra)#acessa do dicionario melaine@... o valor da chave a dentro da chave extra
