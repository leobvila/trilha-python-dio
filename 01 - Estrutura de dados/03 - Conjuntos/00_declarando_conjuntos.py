#conjunto (dados set) coleçao de objetos nao repitidos. elinina iteens duplicados dentro de um objeto iteravel

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}
nome = set("LeOnardo")


linguagens = {"python", "java", "python",}
print(linguagens)