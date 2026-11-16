idade = input("Insira sua idade: ")
print(idade)

altura = input("insira sua altura: ")
print(altura)

#Bloco C Programas curtos
#exercicio 1 

total_segundos = int(input("me de alguns segundos para converter para minutos e horas: "))

horas = total_segundos // 3600
resto = total_segundos % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{total_segundos} segundos = {horas} h {minutos} m {resto} s")


#exercicio 2

preco_sem_iva = float(input("Preco sem IVA: "))

iva = preco_sem_iva * 0.23
preco_final = preco_sem_iva + iva

print(f"IVA (23%): {iva:.2f} EUR")
print(f"Preco final: {preco_final:.2f} EUR")

#exercicio 3

numero = int(input("Numero: "))

centenas = numero // 100
dezenas = (numero // 10) % 10
unidades = numero % 10

soma = centenas + dezenas + unidades

print("Soma dos algarismos:", soma)

#exercicio 4

nota1 = float(input("Nota numero 1: "))
nota2 = float(input("Nota numero 2: "))
nota3 = float(input("Nota numero 3: "))

media = (nota1 + nota2 + nota3) / 3

nota_mais_alta = max(nota1, nota2, nota3)
nota_mais_baixa = min(nota1, nota2, nota3)

diferenca = nota_mais_alta - nota_mais_baixa

print(f"Media do aluno: {media:.1f}")
print(f"Diferenca entre a nota mais alta e mais baixa: {diferenca:.1f}")

#exercicio 5

total_centimos = int(input("Total em centimos: "))
numero_pessoas = int(input("Numero de pessoas: "))

centimos_por_pessoa = total_centimos // numero_pessoas
sobram = total_centimos % numero_pessoas

euros = centimos_por_pessoa // 100
centimos = centimos_por_pessoa % 100

print(f"Cada pessoa paga: {euros},{centimos} EUR")
print(f"Sobram: {sobram} centimos")

#exercicio 6

import math

raio = float(input("Raio da esfera: "))

volume = (4 / 3) * math.pi * raio ** 3

print(f"Volume da esfera: {volume:.2f} cm³")

#exercicio 7

largura = float(input("Me de uma largura: "))
altura = float(input("Me de uma altura: "))

area = largura * altura
perimetro = 2 * (largura + altura)

diagonal = (largura ** 2 + altura ** 2) ** 0.5

print(f"A area do retangulo: {area}")
print(f"O perimetro do retangulo e: {perimetro}")
print(f"A diagonal do retangulo e: {diagonal:.2f}")

#exercicio 8

valor = int(input("Valor em centimos: "))

moedas50 = valor // 50
valor = valor % 50

moedas20 = valor // 20
valor = valor % 20

moedas10 = valor // 10
valor = valor % 10

moedas5 = valor // 5
valor = valor % 5

moedas2 = valor // 2
valor = valor % 2

moedas1 = valor // 1
valor = valor % 1

print("50c:", moedas50)
print("20c:", moedas20)
print("10c:", moedas10)
print("5c:", moedas5)
print("2c:", moedas2)
print("1c:", moedas1)


#exercicio 9

quilometros = float(input("Quilómetros percorridos: "))
litros = float(input("Litros gastos: "))

consumo = (litros / quilometros) * 100

print(f"Consumo: {consumo:.2f} L/100km")


#exercicio 10

segundos = int(input("Segundos: "))

horas = segundos // 3600
segundos = segundos % 3600

minutos = segundos // 60
segundos = segundos % 60

print(f"Tempo: {horas:02d}:{minutos:02d}:{segundos:02d}")


#exercicio 11

celsius = float(input("Temperatura em Celsius: "))

fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

print(f"Fahrenheit: {fahrenheit:.1f}")
print(f"Kelvin: {kelvin:.1f}")


#exercicio 12

numero = int(input("Numero: "))

primeiro = numero // 1000
ultimo = numero % 10

trocados = ultimo * 1000 + (numero % 1000 // 10) * 10 + primeiro

print("Primeiro:", primeiro)
print("Ultimo:", ultimo)
print("Trocados:", trocados)

#Bloco D Problemas integradores

#exercicio 1

TAXA_ANUAL = 3.5

capital_inicial = int(input("Digite o capital inicial: "))
anos = int(input("Digite a quantidade de anos: "))

capital_acumulado = capital_inicial * (1 + TAXA_ANUAL / 100) ** anos

juros_ganhos = capital_acumulado - capital_inicial

print(f"Capital Inicial: {capital_inicial}")
print(f"Taxa anual (%): {TAXA_ANUAL}")
print(f"Anos: {anos}")
print(f"Capital final: {capital_acumulado:.2f}")
print(f"Juros ganhos: {juros_ganhos:.2f}")


#exercicio 2

loja = "Anderson TIS93"
data = "2026-08-19"
TAXA_IVA = 0.23

quantidade_artigo = int(input("Qual a quantidade de artigo? "))
preco_artigo = float(input("Qual o Preço sem IVA? "))
desconto_comercial = float(input("qual a (%) de Desconto? "))

valor_bruto = quantidade_artigo * preco_artigo - desconto_comercial
valor_final = valor_bruto * (1 + TAXA_IVA)
iva = valor_bruto * TAXA_IVA


linha = "=" * 40
print(linha)
print(f"{loja:^40}")
print(f"{'Data: ' + data:^40}")
print(linha)
print(f"{'Artigo (x' + str(quantidade_artigo) + ')':<28}{preco_artigo * quantidade_artigo:>12.2f}")
print("-" * 40)
print(f"{'Subtotal':<28}{valor_bruto:>12.2f}")
print(f"{'IVA (23%)':<28}{iva:>12.2f}")
print(linha)
print(f"{'TOTAL':<28}{valor_final:>12.2f}")
print(linha)


#exercicio 3

parafusos = int(input("Total de parafusos: "))

caixas = parafusos // 12
parafusos_soltos = parafusos % 12

paletes = caixas // 40
caixas_soltas = caixas % 40

print(f"Paletes completas: {paletes}")
print(f"Caixas soltas: {caixas_soltas}")
print(f"Parafusos soltos: {parafusos_soltos}")


#exercicio 4

hora_atual = int(input("Hora atual (HH): "))
minutos = int(input("Minutos atuais: "))
minutos_adicionar = int(input("Minutos a adicionar: "))

total_minutos = hora_atual * 60 + minutos + minutos_adicionar

dias = total_minutos // 1440
total_minutos = total_minutos % 1440

nova_hora = total_minutos // 60
novos_minutos = total_minutos % 60

print(f"Nova hora: {nova_hora:02d}:{novos_minutos:02d}")
print(f"Dias passados: {dias}")


#exercicio 5

teste = float(input("Nota do teste: "))
trabalho = float(input("Nota do trabalho: "))
assiduidade = float(input("Nota da assiduidade: "))

media = teste * 0.60 + trabalho * 0.30 + assiduidade * 0.10

final_round = round(media)
final_int = int(media)

print(f"Média ponderada: {media:.2f}")
print(f"Classificação com round(): {final_round}")
print(f"Classificação com int(): {final_int}")