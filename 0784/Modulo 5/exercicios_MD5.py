def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)
 
print(fatorial(3))

#--------------------------------
def soma(lista):
    if lista == []:
        return 0
    return lista[0] + soma(lista[1:])
 
print(soma([5, 10, 15]))

#--------------------------------
triplo = lambda x: x * 3
print(triplo(4))

#--------------------------------
palavras = ["casa", "oi", "programa"]
r = sorted(palavras, key=lambda p: len(p))
print(r)

#--------------------------------
nums = [1, 2, 3, 4]
print(list(map(lambda x: x + 10, nums)))
print(list(filter(lambda x: x > 2, nums)))

#--------------------------------
def contar(n):
    n= (n - 1)
    print(n)
 
contar(5)

#--------------------------------
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)
print(fatorial(3))

#--------------------------------
quadrado = lambda x: x * x
print(quadrado(5))

#--------------------------------
nums = [1, 2, 3]
resultado = map(lambda x: x * 2, nums)
print(list(resultado))
#--------------------------------
def soma(lista):
    if lista == []:
        return 0
    return lista[0] + soma(lista[1:])

#--------------------------------
def contagem(n):
    if n == 0:
        print("Lançar!")
        return
    print(n)
    contagem(n - 1)

contagem(5)

#--------------------------------
def soma_ate(n):
    if n == 0:
        return 0
    return n + soma_ate(n - 1)

print(soma_ate(5))

#--------------------------------
def potencia(base,exp):
    if exp == 0:
        return 1
    return base ** exp

print(potencia(2,4))

#--------------------------------
alunos = [("Ana", 17), ("Rui", 15), ("Ze", 19)]

resultado = sorted(alunos, key=lambda x: x[1])

print(resultado)

#--------------------------------
palavras = ["sol", "lua", "estrela"]

comprimentos = list(map(lambda x: len(x), palavras))
print(comprimentos)
#--------------------------------
resultado = list(filter(lambda x: len(x) > 3, palavras))
print(resultado)

#--------------------------------
def contar_pares(lista):
    if lista == []:
        return 0
    
    if lista[0] % 2 == 0:
        return 1 + contar_pares(lista[1:])
    else:
        return contar_pares(lista[1:])

print(contar_pares([1, 2, 4, 7, 8]))

#--------------------------------
def inverter(texto):
    if texto == "":
        return ""
    return texto[-1] + inverter(texto[:-1])

print(inverter("Python"))

#--------------------------------
def maximo(lista):
    if len(lista) == 1:
        return lista[0]

    resto = maximo(lista[1:])

    if lista[0] > resto:
        return lista[0]
    else:
        return resto

print(maximo([4, 9, 2, 7, 5]))

#--------------------------------

produtos = [("Pão", 1.2), ("Leite", 0.9), ("Café", 3.5)]

ordenados = sorted(produtos, key=lambda x: x[1])
print(ordenados)

baratos = list(filter(lambda x: x[1] < 2, ordenados))
print(baratos)

nomes = list(map(lambda x: x[0], baratos))
print(nomes)

#--------------------------------

def contar_letra(palavra, letra):
    if palavra == "":
        return 0

    if palavra[0] == letra:
        return 1 + contar_letra(palavra[1:], letra)
    else:
        return contar_letra(palavra[1:], letra)


print(contar_letra("banana", "a"))

def f(x):
    print(x * 2)
 
r = f(3)
print(r)



d = {"x": 1, "y": 2}
d["z"] = 3
print(len(d))


a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)


