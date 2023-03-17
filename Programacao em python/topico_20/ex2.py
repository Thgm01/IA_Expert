alunos = {'Thiago': 0.0,
          'Luana' : 0.0,
          'Lucas' : 0.0}

for aluno, nota in alunos.items():
    note = float(input(f"Write the {aluno}'s grade: "))
    alunos[aluno] = note

soma = 0
for i in alunos.values():
    soma += i

media = soma/len(alunos.values())
print(f'The mean of these students is {media}')