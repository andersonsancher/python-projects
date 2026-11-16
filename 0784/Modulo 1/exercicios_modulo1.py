#A1.  Qual é a saída deste programa?
def ola():
    print("Ola!")

ola()
ola()
ola()
#A3.  Qual é o valor final de x?
def triplo(n):
    return n * 3
 
x = triplo(4)
print(x)

#A2.  Escreve o que aparece no ecrã e por que ordem.
def linha():
    print("---")
 
print("inicio")
linha()
print("fim")

#A4.  O que imprime este programa? Cuidado com o return.
def teste():
    return "A"
    return "B"
    print("C")
 
print(teste())

#A5.  Qual é a saída? Repara na diferença entre print e return.
def mostra(n):
    print(n * 2)
 
def devolve(n):
    return n * 2
 
mostra(5)
resultado = devolve(5)
print(resultado)

#A6.  O que imprime a última linha e porquê?
def saudar(nome):
    print("Ola", nome)
 
r = saudar("Ana")
print(r)

#A7.  Indica os dois valores impressos.
def divide(a, b):
    return a // b, a % b
 
q, r = divide(20, 6)
print(q)
print(r)

#B1.  Este programa não mostra nada no ecrã. Porquê? Corrige-o.
def bemvindo():
    print("Bem-vindo ao curso!")
bemvindo()

#B2.  O Python dá IndentationError. Corrige o código.
def contar():
    print("1")
    print("2")
contar()

#B3.  A função devia devolver o dobro, mas x fica a None. Corrige.
def dobro(n):
    return n * 2
 
x = dobro(8)
print(x)

#B4.  Esta chamada dá NameError: name 'saudar' is not defined. Explica e corrige.

 
def saudar():
    print("Ola!")
saudar()

#B5.  O programador queria executar a função, mas nada acontece. Corrige a última linha.
def menu():
    print("1 - Novo")
    print("2 - Sair")
 
menu()

#B6.  A mensagem “adeus” nunca aparece. Explica porquê.
def despedir():
    print("adeus")
    return "fim"
    
 
print(despedir())

#C1.  Cria uma função chamada apresentar() que imprima o teu nome e o curso em duas linhas. Chama-a a seguir.
def apresentar():
    print("Anderson Campos")
    print("Técnico de informática e Sistemas")
apresentar()

#C2.  Cria uma função quadrado(n) que devolva (com return) o quadrado de n. Testa-a imprimindo quadrado(7).
def quadrado(n):
    return n * n 

print(quadrado(7))

#C3.  Escreve uma função area_retangulo(base, altura) que devolva a área. Mostra a área de um retângulo 5 por 3.

def area_retangulo(base, altura):
    return base * altura

resultado = area_retangulo(5, 3)
print(resultado)

#C4.  Cria uma função e_par(n) que devolva True se n for par e False caso contrário (usa o operador %).
def e_par(n):
    return n % 2 == 0
print(e_par(4))  
print(e_par(7))  

#C5.  Escreve uma função maior(a, b) que devolva o maior dos dois números recebidos.
def maior(a, b):
    if a > b:
        return a
    else:
        return b
print(maior(10, 5))   
print(maior(3, 8))    

#C6.  Cria uma função soma_e_media(a, b, c) que devolva dois valores: a soma e a média dos três números.
def soma_e_media(a, b, c):
    soma = a + b + c
    media = soma / 3
    return soma, media
s, m = soma_e_media(6, 12, 18)
print("Soma:", s)
print("Média:", m)

#C7.  Escreve uma função com uma docstring: converter_para_euros(dolares) que devolva o valor em euros (usa a taxa 0.92). Chama help() sobre ela.
def converter_para_euros(dolares):
    """
    Converte um valor em dólares (USD) para euros (EUR).
    
    Parâmetros:
    dolares (float): Valor em dólares a ser convertido.
    
    Retorna:
    float: Valor convertido em euros com a taxa fixa de 0.92.
    """
    taxa = 0.92
    return dolares * taxa

valor_euros = converter_para_euros(100)
print("100 Dólares =", valor_euros, "Euros")
help(converter_para_euros)

#D Problemas integradores
#D1.  Escreve uma função conta_bancaria(saldo, deposito, levantamento) que devolva o saldo final. A seguir, imprime o saldo final para um saldo inicial de 100, um depósito de 50 e um levantamento de 30.
def conta_bancaria(saldo,deposito,levantamento):
    saldo_final = saldo + deposito - levantamento
    return saldo_final
saldo = conta_bancaria(100,50,30)
print (f"Seu saldo final é : {saldo:.2f}€")

#D2.  Cria duas funções: preco_com_iva(preco) que devolve o preço com 23% de IVA, e mostrar_fatura(nome, preco) que imprime uma fatura simples usando a primeira função. Testa com um produto à tua escolha.
def preco_com_iva(preco):
    return preco * 1.23


def mostrar_fatura(nome, preco):
    preco_final = preco_com_iva(preco)
    print("----- FATURA -----")
    print("Produto:", nome)
    print("Preço sem IVA:", preco)
    print("Preço com IVA:", preco_final)


mostrar_fatura("Teclado", 25)


#D3.  Escreve uma função classificar(nota) que devolva a menção correspondente: “Reprovado” (< 10), “Suficiente” (10 a 13), “Bom” (14 a 17) ou “Muito Bom” (18 a 20). Testa com três notas diferentes.

def classificar(nota):
    if nota < 10:
        return "Reprovado"
    elif nota <= 13:
        return "Suficiente"
    elif nota <=17:
        return "Bom"
    else:
        return "Muito Bom"
print(classificar(8))
print(classificar(12))

#D4.  Constrói um pequeno programa com: uma função titulo() que imprime um cabeçalho, uma função imc(peso, altura) que devolve o Índice de Massa Corporal (peso / altura ao quadrado), e código principal que imprime o cabeçalho e o IMC de uma pessoa com 70 kg e 1.75 m.

def titulo():
    print("----- CÁLCULO DO IMC -----")


def imc(peso, altura):
    return peso / (altura ** 2)


titulo()

resultado = imc(70, 1.75)
print("IMC:", resultado)

