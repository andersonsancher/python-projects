def titulo():
    print("---")
def imc(peso, altura):
    peso = 70
    altura = 1.75
    indice_massa_corporal = imc(float(peso / altura * 2))
print(f"o IMC de uma pessoa com 70kg e 1.75m é: {imc}")