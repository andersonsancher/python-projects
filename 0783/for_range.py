
#exemplo
"""nomes = ["Ana", "Bruno", "Carla"]
notas = [14, 11, 17]

for nome, nota in zip (nomes, notas):
    estado = "Aprovado" if nota >= 10 else "Reprovado"
    print("-" * 40)
    print(f"|{nome:10s}|{nota:5d} | {estado:^25}")
    print("-" * 40)

#exemplo

#notas = [14, 11, 17, 8, 20]

print(notas[0]) # 14, primeiro
print(notas[-1]) # 20, ultimo
print(len(notas)) #5"""

#exemplo

notas = []
quantos = 1

for i in range(1, quantos + 1):
    nota = float(input(f"Nota {i}: "))
    notas.append(nota)
print(notas)

#Exercício 1. acumulador com for

total = 0
for i in range(1, 6):
    total += i
print(total)

#exercicio 2. Produto
p = 1
for i in range(2, 5):
    p *= i
print(p)

#exercicio 3. alterar sobre o texto
conta = 0
for c in "Programacao":
    if c in "aeiou":
        conta += 1
print(conta)

#exercicio 4. Índices

palavra = "Python"
for i in range(len(palavra)):
    if i % 2 == 0:
        print(palavra[i], end="")
print()

#exercicio 5. Passo negativo
s = ""
for i in range(4, -1, -1):
    s += str(i)
print(s)

#Exercício 6.  enumerate
for i, letra in enumerate("abc", start=1):
    print(i, letra)

#Exercicio 7. zip com comprimentos diferentes
nomes = ["Ana", "Bruno", "Carla"]
notas = [14, 11]

for nome, nota in zip(nomes, notas):
    print(nome, nota)

#Exercicio 8. Lista construida em ciclo

valores = []
for i in range(1, 6):
    print(i)
    valores.append(i * i)
    print(valores)
print(valores)
print(sum(valores), max(valores))

#Exercicio 9. Variável após o ciclo

for i in range(3):
    pass
print(i)

#Bloco B. Correção de código

#Exercício 1. contar até n

n = 10
for i in rage(n):
    print(i)
