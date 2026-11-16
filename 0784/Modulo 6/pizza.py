# programa PIZZA
print(f"-----PIZZA-----")
print("Bem vindo ao programa PIZZA")
tamanho = input("Escolha o tamanho da pizza\n(normal ou maxi): ")
print("\nEmenta de pizzas")
print(" Margarita\n Peperoni\n Carbonara\n Romana\n Havaina")
escolha = input("\nEscolha a pizza da ementa: ").lower()

print("\nBebidas\n Agua\n Coca-cola\n Cerveja\n Sumol\n")
bebida = input("Escolha a bebida: ").lower()
nif = input("\nInsira o seu contribuinte: ")
total = 0

ingredientes_margarita = ["molho tomate", "queijo"]
ingredientes_peperoni = ["molho tomate", "queijo", "peperoni"]
ingredientes_carbonara = ["natas", "queijo", "cogumelos"]
ingredientes_romana = ["fiambre", "azeitonas", "pimentos"]
ingredientes_havaiana = ["fiambre", "ananas", "queijo"]

print("\n-----Pedido-----")
print(f"Tamanho: {tamanho}")
print(f"Pizza: {escolha}")
print(f"Bebida: {bebida}")

preco_margarita = 12.99
preco_peperoni = 16.0
preco_carbonara = 18.0
preco_romana = 20.0
preco_havaiana = 22.0

preco_agua = 1.5
preco_cola = 2.0
preco_cerveja = 1.0
preco_sumol = 2.0

match escolha:
    case "margarita":
        print(f"Ingredientes: {', '.join(ingredientes_margarita)}")
    case "peperoni":
        print(f"Ingredientes: {', '.join(ingredientes_peperoni)}")
    case "carbonara":
        print(f"Ingredientes: {', '.join(ingredientes_carbonara)}")
    case "romana":
        print(f"Ingredientes: {', '.join(ingredientes_romana)}")
    case "havaiana":
        print(f"Ingredientes: {', '.join(ingredientes_havaiana)}")
    case _:
        print("Não temos a 🍕 que escolheu 😒.")



print("\n-----FATURA-----")
print(f"NIF: {nif}")
match escolha:
    case "margarita":
        if tamanho == "normal":
            total += preco_margarita
            print(f"Pizza {escolha}: {preco_margarita:.2f}€")
        else:
            total += preco_margarita + 4.0
            print(f"Pizza {escolha}: {preco_margarita + 4.0:.2f}€")
    case "peperoni":
        if tamanho == "normal":
            total += preco_peperoni
            print(f"Pizza {escolha}: {preco_peperoni:.2f}€")
        else:
            total += preco_peperoni + 4.0
            print(f"Pizza {escolha}: {preco_peperoni + 4.0:.2f}€")
    case "carbonara":
        if tamanho == "normal":
            total += preco_carbonara
            print(f"Pizza {escolha}: {preco_carbonara:.2f}€")
        else:
            total += preco_carbonara + 4.0
            print(f"Pizza {escolha}: {preco_carbonara + 4.0:.2f}€")
    case "romana": 
        if tamanho == "normal": 
            total += preco_romana
            print(f"Pizza {escolha}: {preco_romana:.2f}€")
        else: 
            total += preco_romana + 4.0
            print(f"Pizza {escolha}: {preco_romana + 4.0:.2f}€")
    case "havaiana":
        if tamanho == "normal":
            total += preco_havaiana
            print(f"Pizza {escolha}: {preco_havaiana:.2f}€")
        else:
            total += preco_havaiana + 4.0
            print(f"Pizza {escolha}: {preco_havaiana + 4.0:.2f}€")

match bebida:
    case "agua":
        total += preco_agua
        print(f"Bebida {bebida}: {preco_agua:.2f}€")
    case "coca-cola":
        total += preco_cola
        print(f"Bebida {bebida}: {preco_cola:.2f}€")
    case "cerveja":
        total += preco_cerveja
        print(f"Bebida {bebida}: {preco_cerveja:.2f}€")
    case "sumol":
        total += preco_sumol
        print(f"Bebida {bebida}: {preco_sumol:.2f}€")
    case _:
        print("Não temos essa bebida 😒.")

print(f"Total: {total:.2f}€")
print(f"IVA 23%: {total * 0.23:.2f}€")
print(f"Total c/IVA: {total * 1.23:.2f}€")