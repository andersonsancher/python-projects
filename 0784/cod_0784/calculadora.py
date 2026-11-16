def somar(n1,n2):
    return n1 + n2
def subtrair(n1,n2):
    return n1 - n2
def multiplicar(n1,n2):
    return n1 * n2
def dividir(n1,n2):
    return n1 / n2

print("-" * 30)
print(f'{"CALCULADORA":^30}')
print("-" * 30)

print("Bem vindo ao programa Calculadora.")
print("1-Somar")
print("2-Subtrair")
print("3-Multiplicar")
print("4-Dividir")
print("0-Sair")

numero1= float(input("Insira o primeiro número: "))
numero2= float(input("Insira o segundo número: "))
operacao = input("Insira o número da operação aritmética: ")


match operacao:
    case "1":
        print(f"O número {numero1} + {numero2}= {somar(numero1, numero2):.2f}")
    case "2":
        print(f"O número {numero1} - {numero2}= {subtrair(numero1, numero2):.2f}")
    case "3":
        print(f"O número {numero1} * {numero2}= {multiplicar(numero1, numero2):.2f}")
    case "4":
        if numero2 == 0:
            print(f"Não se pode dividir um número por zero.")
        else:
            print(f"O número {numero1} / {numero2}= {dividir(numero1, numero2):.2f}")
    case "0":
        print("Até a próxima.")
        exit()
    case _:
        print("Opção inválida.")

        