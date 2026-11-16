# As variaveis definidas dentro de uma função apenas são vistas pela função

def somar():
    x = 5
    print(x)

# print(x) esta variável não é reconhecida fora da função
somar() # apenas temos acesso ao seu valor chamando a função

# Variaveis declaradas no bloco principal podem  ser
#  utilizadas dentro da função mas não pode ser alteradas
mensagem = "Prestem atenção ao formador"

def msg():
    mensagem = "Estamos quase a ir embora"
    print(mensagem)

msg()
print(mensagem)

# a palavra "global" permite alterar o valor de uma variavel dentro da função

numero = 10

def ler_numero():
    global numero
    numero += 3
    print(numero)

ler_numero()


# para alterar uma 
# váriavel de uma função dentro de outra função aninhada utilizamos a palavra nonlocal 

def adicionar():
    n = 3
    def incrementar():
        nonlocal n 
        n += 5
        print(n)
    incrementar()
adicionar()


def externa():
    total = 0
    
    def interna():
       nonlocal total
       total += 5
       print(total)
    interna()
    
 
externa()



lista = [1, 2, 3]
print(f"{lista}((4, 5, 6))")


iva = 0.23
 
def preco(base):
    return base * (1 + iva)
    
    

print(preco(10))


mensagem = "Oi"

def mostrar():
    global mensagem
    mensagem = "Olá"
    print(mensagem)

mostrar()


pontos = 0

def ganhar(n):
    global pontos 
    print(n + pontos)

ganhar(10)
ganhar(20)
print(ganhar)


variavel = "global"

def demonstrar():
    variavel = "local"
    print(variavel)

demonstrar()
print(variavel)



def contador():
    total = 0
    def incrementar():
        nonlocal total
        total += 1
        print(total)
    incrementar()
        
contador()


pontos = 0

def ganhar(n): 
    print(n + pontos)
    return ganhar
ganhar(10)
ganhar(20)



# --- 
ano = input("Qual o ano atual ?")
idade = input("Qual sua idade ? ")

def AnoNascimento(self, ano, idade):
    self.ano = ano
    self.idade = idade

resultado = ano - idade


print(f"Seu ano de nascimento é ")