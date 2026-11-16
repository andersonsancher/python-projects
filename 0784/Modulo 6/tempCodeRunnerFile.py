turma_a = ["Ana", "Rui", "Zé", "João"]
turma_b = ["Rui", "Zé", "Maria", "Pedro"]

a = set(turma_a)
b = set(turma_b)

print("Nas duas turmas:", a & b)
print("Só na turma A:", a - b)
print("Só na turma B:", b - a)
print("Total de alunos distintos:", len(a | b))