total = 0

while True:
    preco = float(input("Preço do produto (0 para sair): "))

    if preco == 0:
        break

    total += preco

    print("Total da compra: ", total)