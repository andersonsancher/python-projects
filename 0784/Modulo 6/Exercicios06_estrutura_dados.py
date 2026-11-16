letras = ["a", "b", "c", "d", "e"]
print(letras[0])
print(letras[-1])
print(letras[1:3])
print(letras[::-1])

nums = [3, 1, 2]
nums.append(5)
nums.insert(0, 9)
nums.sort()
print(nums)


ponto = (10, 20)
x, y = ponto
print(x + y)


aluno = {"nome": "Ana", "idade": 25}
print(aluno["nome"])
print(aluno.get("email", "sem email"))
aluno["idade"] = 26
print(aluno["idade"])

a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a | b)
print(a & b)
print(a - b)

lista = [1, 1, 2, 3, 3, 3]
print(set(lista))
print(len(set(lista)))


frutas = ["maca", "banana"]
print(frutas)

aluno = {"nome": "Ana"}
print(aluno)


t = (42,)
print(type(t))



cidades = ["Lisboa", "Porto", "Braga", "Coimbra", "Faro"]

print(cidades[0])
print(cidades[-1])
print(cidades[1:4])



coordenadas = (3, 7)

x, y = coordenadas

print(x + y)

a = 10
b = 20

a, b = b, a

print(a)
print(b)


produto = {
    "nome": "Teclado",
    "preco": 25.99,
    "stock": 10
}

for chave, valor in produto.items():
    print(chave, valor)


nums = [5, 2, 8, 1]

nums.append(10)
nums.remove(2)
nums.sort()

print(nums)
print(len(nums))


cidades = ["Lisboa", "Porto", "Braga", "Coimbra", "Faro"]

print(cidades[0])
print(cidades[-1])
print(cidades[1:4])



produto = {
    "nome": "Teclado",
    "preco": 25.99,
    "stock": 10
}

for chave, valor in produto.items():
    print(chave, valor)


nomes = ["ana", "rui", "ana", "ze", "rui"]

unicos = set(nomes)

print(unicos)
print(len(unicos))


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("União:", a | b)
print("Interseção:", a & b)
print("Diferença:", a - b)

agenda = {
    "nome": "Maria",
    "telefone": 924352653,

    "nome": "João",
    "telefone": 924352651,

    "nome": "Marco",
    "telefone": 924352654,
    }

for chave, valor in agenda.items():
    print(chave, valor)


agenda = {}


agenda["Ana"] = "912345678"
agenda["Rui"] = "923456789"
agenda["Zé"] = "934567890"


agenda["Rui"] = "999999999"


del agenda["Zé"]


for nome, telefone in agenda.items():
    print(nome, telefone)


alunos = [
    {"nome": "Ana", "nota": 10},
    {"nome": "Rui", "nota": 15},
    {"nome": "Zé", "nota": 8}
]

for aluno in alunos:
    if aluno["nota"] >= 10:
        print(aluno["nome"])


compras = ["pao", "leite", "pao", "ovos", "leite", "pao"]

contagem = {}

for item in compras:
    contagem[item] = contagem.get(item, 0) + 1

print(contagem)        


turma_a = ["Ana", "Rui", "Zé", "João"]
turma_b = ["Rui", "Zé", "Maria", "Pedro"]

a = set(turma_a)
b = set(turma_b)

print("Nas duas turmas:", a & b)
print("Só na turma A:", a - b)
print("Só na turma B:", b - a)
print("Total de alunos distintos:", len(a | b))