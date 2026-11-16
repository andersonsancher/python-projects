# While - O loop while executa um determinado código até que uma condição seja avaliada como falsa

linguagem = "Python"
incremento = 0 

while incremento <=len(linguagem):
    print(linguagem[incremento])
    incremento += 1


# Conta Bancária

print("PROGRAMA CONTA BANCÁRIA")
print()
print("1 - Consultar Saldo")
print("2 - Depósito")
print("3 - Levantamento")
print("4 - Sair")

nome = input("Nome: ")
saldo = 500.00
transacoes_depositos = 0
transacoes_levantamentos = 0
LIMITE_LEVANTAMENTO = 200.00


print(f"Bem vindo: {nome}")

while True:
    opcao = input("Escolha a operação bancária: ")
    if opcao == "1":
        print(f"Saldo: {saldo}")
    elif opcao == "2":
        deposito = float(input("Insira o valor de depósito: "))
        saldo += deposito
        transacoes_depositos += 1
        print(f"Depositou: {deposito:.2f} euros.")
    elif opcao == "3":
        levantamento = float(input("Qual o valor deseja levantar? "))
        if levantamento > saldo:
            print("O valor a levantar é superior ao seu saldo, insira um valor de levantamento igual ou inferior ao saldo. ")
        elif levantamento > LIMITE_LEVANTAMENTO:
            print(f"Já excedeu o limite de levantamentos: {LIMITE_LEVANTAMENTO}€ diário.")
        else:
            saldo -= levantamento
            transacoes_levantamentos += 1
            print(f"Levantou: {levantamento:.2f} euros.")
    elif opcao == "4":
        print("Obrigado, até a próxima! ")
        break
    else:
        print("A opção que inseriu é inválida, tente novamente.")

print(f"Total de depósitos: {transacoes_depositos}")
print(f"Total de levantamentos: {transacoes_levantamentos}")
print(f"Total de transações: {transacoes_levantamentos + transacoes_depositos}")

# EURO MILHÕES MANUAL

# - pedir ao utilizador 5 números de 1 a 50 - chave 
# - pedir ao utilizador 2 números de 1 a 12 - estrelas
# - validar os números inseridos pelo utilizador
# - imprimir a chave e as estrelas
# - utilizar loop while
# - adicionar número a lista chave.append()

#Minha versão sem CHAT
chaves = []
estrelas = []



while True:
    print("EURO MILHÕES")
    print()
    print("1 - Inserir Chave")
    print("2 - Inserir Estrela")
    print("3 - Saída")
    opcao = input("Escolha a opção: ")  
    num_estrelas = 0
    num_chave = 0
    while True:
        if opcao == "1":
            num_chave = int(input("Insira 5 números de 1 a 50: "))
        elif num_chave < 1 or num_chave > 50:
            print("Escreva um número de 1 a 50.")
        elif num_chave in chaves:
            print("O número é repetido.")
        else:
            chaves.append(num_chave)
        if len(chaves) > 4:
            break
    while True:
        if opcao == "2":
            num_estrelas = int(input("Insira 2 números de 1 a 12: "))
        elif num_estrelas < 1 or num_estrelas > 12:
            print("Escreva um número de 1 a 12.")
        elif num_estrelas in estrelas:
            print("O número é repetido.")
       
        else:
            estrelas.append(num_estrelas)
        if len(estrelas) > 1:
            break
        if opcao == "3":
            print("Obrigado, até a próxima.")
            break

    resultado = " ".join(map(str,chaves))
    print("O números Chaves escolhidos foram: ", resultado)
    resultado2 = " ".join(map(str,estrelas))
    print("O números Estrelas escolhidos foram: ", resultado2)

    #com a melhoria do chat 
    # EURO MILHÕES MANUAL

    # - pedir ao utilizador 5 números de 1 a 50 - chave 
    # - pedir ao utilizador 2 números de 1 a 12 - estrelas
    # - validar os números inseridos pelo utilizador
    # - imprimir a chave e as estrelas
    # - utilizar loop while
    # - adicionar número a lista chave.append()

    chaves = []
    estrelas = []

    while True:
        print()
        print("EURO MILHÕES")
        print()
        print("1 - Inserir Chave")
        print("2 - Inserir Estrela")
        print("3 - Saída")

        opcao = input("Escolha a opção: ")

    
        if opcao == "1":
            while len(chaves) < 5:
                num_chave = int(input("Insira um número de 1 a 50: "))

            if num_chave < 1 or num_chave > 50:
                print("Escreva um número de 1 a 50.")

            elif num_chave in chaves:
                print("O número é repetido.")

            else:
                chaves.append(num_chave)
                print("Número adicionado!")

    # INSERIR ESTRELAS
        elif opcao == "2":
            while len(estrelas) < 2:
                num_estrelas = int(input("Insira um número de 1 a 12: "))

            if num_estrelas < 1 or num_estrelas > 12:
                print("Escreva um número de 1 a 12.")

            elif num_estrelas in estrelas:
                print("O número é repetido.")

            else:
                estrelas.append(num_estrelas)
                print("Estrela adicionada!")

    # SAIR
        elif opcao == "3":
            print("Obrigado, até a próxima.")
            break

        else:
            print("Opção inválida.")

    # MOSTRAR RESULTADO
        if len(chaves) == 5 and len(estrelas) == 2:
            resultado = " ".join(map(str, chaves))
            resultado2 = " ".join(map(str, estrelas))

        print()
        print("Os números da Chave escolhidos foram:", resultado)
        print("As Estrelas escolhidas foram:", resultado2)  

     