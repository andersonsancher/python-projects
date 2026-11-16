

#C1.  Cria uma função saudar(nome) que imprima “Bem-vindo, <nome>!”. Testa com dois nomes.
def saudar(nome):
    print(f"Bem-vindo, {nome}!")

saudar("Ana")
saudar("Pedro")

#C2.  Escreve uma função area_triangulo(base, altura) que devolva a área (base vezes altura a dividir por 2). Testa com base 6 e altura 4.
def area_triangulo(base, altura):
    return (base * altura) / 2

print(area_triangulo(6, 4))  

#C3.  Cria uma função potencia(base, expoente=2) em que o expoente por omissão é 2. Mostra potencia(5) e potencia(2, 10).
def potencia(base, expoente=2):
    return base ** expoente

print(potencia(5))       
print(potencia(2, 10))   

#C4.  Escreve uma função descontar(preco, percentagem=10) que devolva o preço já com o desconto aplicado. Testa com e sem o segundo argumento.
def descontar(preco, percentagem=10):
    return preco * (1 - percentagem / 100)

print(descontar(100))      
print(descontar(100, 20))  

#C5.  Cria uma função ligar(origem, destino, ida_volta=False) que imprima a viagem. Chama-a uma vez com ida_volta nomeado como True.
def ligar(origem, destino, ida_volta=False):
    if ida_volta:
        print(f"Viagem de ida e volta: {origem} <-> {destino}")
    else:
        print(f"Viagem de ida: {origem} -> {destino}")

ligar("Lisboa", "Porto", ida_volta=True)

#C6.  Escreve uma função criar_email(nome, dominio="escola.pt") que devolva um endereço no formato nome@dominio. Testa com o domínio por omissão e com outro à tua escolha.
def criar_email(nome, dominio="escola.pt"):
    return f"{nome}@{dominio}"

print(criar_email("joao"))                 
print(criar_email("maria", "empresa.com")) 	


#D1.  Cria uma função fatura(produto, preco, quantidade=1,
#  iva=0.23) que devolva o total a pagar (preço vezes quantidade,
#  com IVA). Testa com três chamadas diferentes, usando argumentos nomeados onde fizer sentido.

def fatura(produto, preco, quantidade=1, iva=0.23):
    subtotal = preco * quantidade
    total = subtotal * (1 + iva)
    return round(total, 2)

print(fatura(f"Caderno", 5.0))
print(fatura("Caneta", 1.5, 3))
# usando argumentos nomeados para alterar o IVA e a quantidade
print(fatura("Livro", 20.0, quantidade=2, iva=0.06))

#D2.  Escreve uma função classificar(nota, escala=20) que devolva a percentagem (nota a dividir pela escala, vezes 100). Permite mudar a escala para 100 numa das chamadas.

def classificar(nota, escala=20):
    return (nota / escala) * 100

print(f"{classificar(15)}%")             
print(f"{classificar(85, escala=100)}%")  

#D3.  Constrói uma função registar_utilizador(nome, email, ativo=True, nivel=1) que imprima uma linha com todos os dados. Faz três registos: um só com os obrigatórios, um com nivel diferente e um com ativo a False.

def registar_utilizador(nome, email, ativo=True, nivel=1):
    print(f"Nome: {nome} | Email: {email} | Ativo: {ativo} | Nível: {nivel}")
registar_utilizador("Ana", "ana@email.com")
registar_utilizador("Rui", "rui@email.com", nivel=3)
registar_utilizador("Carlos", "carlos@email.com", ativo=False)

#D4.  Cria uma função calcular_salario(horas, valor_hora=10, bonus=0) que devolva o salário total. A seguir, escreve uma função mostrar_recibo(nome, horas) que use a primeira e imprima o recibo. Testa com um trabalhador à tua escolha.
def calcular_salario(horas, valor_hora=10, bonus=0):
    return (horas * valor_hora) + bonus

def mostrar_recibo(nome, horas):
    salario = calcular_salario(horas, valor_hora=12, bonus=50)
    print(f"--- Recibo de Vencimento ---")
    print(f"Trabalhador: {nome}")
    print(f"Horas trabalhadas: {horas}")
    print(f"Total a receber: {salario}€")

mostrar_recibo("João Silva", 160)

def mostrar(*args):
    print(type(args))
    print(len(args))
 
mostrar("a", "b", "c")

def perfil(**dados):
    for chave, valor in dados.items():
        print(chave, "=", valor)
 
perfil(nome="Ana", idade=25)

def turma(disciplina, *alunos):
    print(disciplina, "tem", len(alunos), "alunos")
 
turma("Python", "Ana", "Rui", "Ze", "Rita")

def somar(a, b, c):
    return a + b + c
 
valores = [4, 5, 6]
print(somar(*valores))

def registar(turma, *alunos, **extras):
    print(turma, alunos, extras)
 
registar("Redes", "Ana", "Rui", sala="B1", ativo=True)

def registar(nome, ativo=True, **extras):
    print(nome, extras, ativo)


def media(*numeros):
    return sum(numeros) / len(numeros)
valores = 10, 20, 30
print(media(*valores))

def dobrar(*args):
    args[0] = args[0] * 2   # erro
    return args


