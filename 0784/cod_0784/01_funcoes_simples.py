#Funções Simples

def cumprimentar ():
    print("Bom dia!")

cumprimentar()
#print(cumprimentar()) print da função dentro de outro print devolve none.

def saudar():
    return "Olá!"

print(f"{saudar()} Nelson!")
print(f"{saudar()} Ana!")
print(f"{saudar()} José! Bem vindo.")

#Funções com parametros e argumentos

def produto(nome_produto, quantidade, preco):
    return (f"O {nome_produto} custa {preco}€ e com a quantidade {quantidade} custa {preco * quantidade}€")

nome_produto = input("Insira o nome do produto: ")
preco_produto = float(input("Insira o preço do produto: "))
quantidade_produto = int(input("Informe a quantidade: "))

print(f"{produto(nome_produto, quantidade_produto, preco_produto)} ")

#Função com parametros e argumentos

def fatura(nome, preco, quantidade=1, iva=1.23):
    return(f"Produto: {nome}\nQuantidade: {quantidade}\nPreço: {preco:.2f}€\nTotal c/IVA: {quantidade * preco * iva:.2f}€")

print(f"FATURA\n{fatura("Teclado", 12.67)}")

#