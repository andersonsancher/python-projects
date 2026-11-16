#Exercicios03_Args_e_Kwargs

#B1:

def turma(disciplina, *alunos):
    print(disciplina, alunos)

#B2:
def registar(nome, ativo=True, **extras):
    print(nome, extras, ativo)

#B3:
def media(*numeros):
    return sum(numeros) / len(numeros)
valores = 10, 20, 30
print(media(*valores))

#B4:
def dobrar(*args):
    return tuple(n * 2 for n in args)

print(dobrar(1, 2, 3))

#B5:
def perfil(nome, idade):
    print(nome, idade)

dados = {"nome": "Ze", "idade": 40}
perfil(**dados)

#C1:
def maximo(*numeros):
    return max(numeros)

print(maximo(3, 7, 2))
print(maximo(10, 1))
print(maximo(5, 8, 2, 9, 1))

#C2:
def juntar(*palavras):
    return " ".join(palavras)

print(juntar("ola", "mundo"))
print(juntar("isto", "e", "um", "teste"))

#C3:
def contar(**kwargs):
    print("Recebi", len(kwargs), "argumentos nomeados")
    print("Chaves:", list(kwargs.keys()))

contar(nome="Ana", idade=25, cidade="Lisboa")

#C4:
def media(*notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

print(media(10, 15, 20, 18, 16))
print(media())

#C5:
def descrever(nome, **caracteristicas):
    print(nome)

    for chave,valor in caracteristicas.items():
        print(f"{chave}: {valor}")


descrever("Cão", idade=3, raca="Pitbull")

#C6:
def soma(*numeros):
    return sum(numeros)

lista = [4, 8, 15, 16]
print(soma(*lista))

#D1:
def fatura(cliente, *produtos, iva=0.23):
    total = sum(produtos) * (1 + iva)
    print(cliente, "-> total com IVA:", round(total, 2))
    return total

fatura("Cliente A", 10, 20, 30)
fatura("Cliente B", 100, iva=0.06)

#D2:
def criar_ficha(nome, **campos):
    ficha = {"Nome": nome}
    return ficha

ficha1 = criar_ficha("Ana", idade=25, cidade="Santarém")
ficha2 = criar_ficha("Paulo", profissao="Programador")
print(ficha1)
print(ficha2)  
    
#D3:
def relatorio(titulo, *linhas, rodape="Fim"):
    print(titulo)
    for linha in linhas:
        print("-", linha)
    print(rodape)

relatorio("Relatório Semanal", "Vendas subiram", "Stock ok")
relatorio("Relatório Final", "Tudo concluído", rodape="Assinado: Gestão")

#D4:

def configurar(**opcoes):
    for chave, valor in opcoes.items():
        print(chave, "=", valor)

definicoes = {"largura": 1920, "altura": 1080, "cor": "azul"}
configurar(**definicoes)