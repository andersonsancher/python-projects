numero_secreto = 7

palpite = int(input("Adivinhe o número: "))

if palpite == numero_secreto:
    print("Acertou!")
elif palpite  numero_secreto:
    print("Muito baixo!")
else:
    print("Muito alto!")