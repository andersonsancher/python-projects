#Bloco C Programas curtos

#exercicio 1

num = int(input("Digite um número: "))

i = 1

while i <= num:
    print(i)
    i += 1


#exercicio 2

numero = int(input("Número positivo: "))

while numero >= 1:
    print(numero)
    numero -= 1

print("Lançamento")

#exercicio 3 

numero = int(input("Digite um número para saber a sua tabuada: "))

i = 1

while i <= 10:
    print(f"{numero:>3} x {i:>2} = {numero * i:>4}")
    i += 1

#exercicio 4 

quantos = int(input("Quantos valores? "))

total = 0
i = 1

while i <= quantos:
    valor = float(input("Valor: "))
    total += valor
    i += 1

print("Soma:", total)

if quantos > 0:
    media = total / quantos
    print(f"Média: {media:.2f}")
else:
    print("Não é possível calcular a média.")

#exercicio 5

quantos = int(input("Quantos números? "))

pares = 0
impares = 0
i = 1

while i <= quantos:
    numero = int(input("Número: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    i += 1

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")

#exercicio 6

quantos = int(input("Quantos valores? "))

i = 1
maior = None
menor = None

while i <= quantos:
    valor = float(input("Valor: "))

    if maior is None or valor > maior:
        maior = valor

    if menor is None or valor < menor:
        menor = valor

    i += 1

print(f"Maior: {maior}")
print(f"Menor: {menor}")

#exercicio 7

numero = int(input("Digite um número inteiro: "))

soma = 0

while numero > 0:
    soma += numero % 10
    numero //= 10

print(f"Soma dos algarismos: {soma}")

#exercicio 8

numero = int(input("Digite um número inteiro: "))

invertido = 0

while numero > 0:
    algarismo = numero % 10
    invertido = invertido * 10 + algarismo
    numero //= 10

print(f"Invertido: {invertido}")

#exercicio 9

total = 0
quantos = 0

valor = float(input("Compra (-1 para terminar): "))

while valor != -1:
    total += valor
    quantos += 1

    valor = float(input("Compra (-1 para terminar): "))

print(f"Compras: {quantos}")
print(f"Total: {total}")

if quantos > 0:
    print(f"Média: {total}, {quantos}")
else:
    print("Não foram registadas compras.")

#exercicio 10

idade = int(input("Idade: "))

while idade < 0 or idade > 130:
    print("Idade inválida.")
    idade = int(input("Idade: "))

print(f"Idade registada: {idade}")

#exercicio 11

OPCOES_VALIDAS = (1, 2, 3, 4)

print("1 - Opção 1")
print("2 - Opção 2")
print("3 - Opção 3")
print("4 - Opção 4")

opcao = int(input("Opção: "))

while opcao not in OPCOES_VALIDAS:
    print("Opção inválida.")
    opcao = int(input("Opção: "))

print(f"Escolheu: {opcao}")

#exercicio 12
base = int(input("Base: "))
expoente = int(input("Expoente: "))

resultado = 1
i = 1

while i <= expoente:
    resultado *= base
    i += 1
print(f"Resultado: {resultado}")

#exercicio 13

numero = int(input("Número: "))

while numero < 0:
    print("Número inválido.")
    numero = int(input("Número: "))

fatorial = 1
i = 1

while i <= numero:
    fatorial *= i
    i += 1

print(f"Fatorial: {fatorial}")

#exercicio 14

PASSWORD = "python123"

tentativas = 3
autorizado = False

while tentativas > 0 and not autorizado:
    palavra = input("Palavra-passe: ")

    if palavra == PASSWORD:
        autorizado = True
    else:
        tentativas -= 1

        if tentativas > 0:
            print("Errada. Restam", tentativas, "tentativa(s).")

if autorizado:
    print("Acesso autorizado.")
else:
    print("Acesso bloqueado.")


#Bloco D Problemas integradores

#exercicico 1

artigos = 0
total_sem_iva = 0

mais_caro = 0
nome_mais_caro = ""

designacao = input("Designação do artigo: ")


while designacao != "fim":
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))
    subtotal = preco * quantidade
    total_sem_iva += subtotal
    artigos += 1
    
    if subtotal > mais_caro:
        mais_caro = subtotal
        nome_mais_caro = designacao
        designacao = input("Designação do artigo: ")
        
        iva = total_sem_iva * 0.23
        total_pagar = total_sem_iva + iva
print("Artigos distintos:", artigos)
print("Total sem IVA:", total_sem_iva)
print("IVA:", iva)
print("Total a pagar:", total_pagar)

if artigos > 0:
        print("Artigo mais caro:", nome_mais_caro)

#exercicio 2
soma = 0
quantidade = 0
maior = None
menor = None
aprovados = 0

nota = float(input("Nota (-1 para terminar): "))

while nota != -1:
    while nota < 0 or nota > 20:
        print("Nota inválida.")
        nota = float(input("Nota (-1 para terminar): "))
        if nota == -1:
            break
    if nota == -1:
        break

    soma += nota
    quantidade += 1

    if maior is None or nota > maior:
        maior = nota
    if menor is None or nota < menor:
        menor = nota
    if nota >= 10:
        aprovados += 1

    nota = float(input("Nota (-1 para terminar): "))

if quantidade > 0:
    media = soma / quantidade
    percentagem = (aprovados / quantidade) * 100
    print(f"Notas introduzidas: {quantidade}")
    print(f"Média: {media:.2f}")
    print(f"Nota mais alta: {maior}")
    print(f"Nota mais baixa: {menor}")
    print(f"Positivas: {aprovados}")
    print(f"Percentagem de aprovação: {percentagem:.2f}%")
else:
    print("Não foram introduzidas notas.")


#exercicio 3
NUMERO_SECRETO = 47
MAX_TENTATIVAS = 7
tentativas = 0
acertou = False

while tentativas < MAX_TENTATIVAS and not acertou:
    palpite = int(input("O teu palpite (1-100): "))

    while palpite < 1 or palpite > 100:
        print("Palpite inválido, tem de estar entre 1 e 100.")
        palpite = int(input("O teu palpite (1-100): "))

    tentativas += 1

    if palpite == NUMERO_SECRETO:
        acertou = True
    elif palpite < NUMERO_SECRETO:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")

if acertou:
    print(f"Acertaste em {tentativas} tentativa(s)!")
else:
    print(f"Não acertaste. O número secreto era {NUMERO_SECRETO}.")

#exercicio 4

numero = int(input("Número decimal: "))

if numero == 0:
    binario = "0"
else:
    n = numero
    binario = ""
    while n > 0:
        resto = n % 2
        binario = str(resto) + binario
        n = n // 2

print(f"Binário: {binario}")

#exercicio 5

saldo = float(input("Valor inicial: "))
deposito = float(input("Depósito mensal: "))
objetivo = float(input("Objetivo: "))

JURO = 0.002
meses = 0

while saldo < objetivo and meses < 600:
    saldo = saldo * (1 + JURO) + deposito
    meses += 1
    if meses % 12 == 0:
        print(f"Fim do ano {meses // 12}: saldo = {saldo:.2f}")

if saldo >= objetivo:
    print(f"Objetivo atingido ao fim de {meses} meses. Saldo final: {saldo:.2f}")
else:
    print(f"Objetivo não atingido em 600 meses. Saldo final: {saldo:.2f}")

#exercicio 6

total = 0
operacoes = 0
opcao = 0

while opcao != 4:
    print("1 - Somar valor ao total")
    print("2 - Ver total")
    print("3 - Repor total a zero")
    print("4 - Sair")

    opcao = int(input("Opção: "))

    while opcao not in (1, 2, 3, 4):
        print("Opção inválida.")
        opcao = int(input("Opção: "))

    if opcao == 1:
        valor = float(input("Valor a somar: "))
        while valor <= 0:
            print("O valor tem de ser positivo.")
            valor = float(input("Valor a somar: "))
        total += valor
        operacoes += 1
    elif opcao == 2:
        print(f"Total atual: {total}")
        operacoes += 1
    elif opcao == 3:
        total = 0
        print("Total reposto a zero.")
        operacoes += 1

print(f"Total acumulado: {total}")
print(f"Operações realizadas: {operacoes}")