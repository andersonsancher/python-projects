soma = 0
quantidade = 0
maior = None
menor = None
aprovados = 0

nota = float(input("Nota (-1 para terminar): "))

while nota != -1:
    while nota < 0 or nota > 20:
        print("Nota inválida.")
        nota = float(input("Nota (-1 para terminar): "))
        if nota == -1:
            break
    if nota == -1:
        break

    soma += nota
    quantidade += 1

    if maior is None or nota > maior:
        maior = nota
    if menor is None or nota < menor:
        menor = nota
    if nota >= 10:
        aprovados += 1

    nota = float(input("Nota (-1 para terminar): "))

if quantidade > 0:
    media = soma / quantidade
    percentagem = (aprovados / quantidade) * 100
    print(f"Notas introduzidas: {quantidade}")
    print(f"Média: {media:.2f}")
    print(f"Nota mais alta: {maior}")
    print(f"Nota mais baixa: {menor}")
    print(f"Positivas: {aprovados}")
    print(f"Percentagem de aprovação: {percentagem:.2f}%")
else:
    print("Não foram introduzidas notas.")