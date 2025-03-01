#[].pop retira o ultimo elemento alguma coisa.pop() se deixar vazio retira o ultimo elemento se colocar um indice retira o indice
#lista vem no padrao de pilha

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python

nome = list("Leonardo")
nome.pop()
nome.pop(4)

print(nome)
