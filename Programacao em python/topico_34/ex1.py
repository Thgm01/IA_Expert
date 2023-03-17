alunos = {'Pedro':9.0, 'Maria':10.0, 'Amilton':7.5}

with open('/home/thiago/Documents/IA_Expert/Programacao em python/topico_34/grade.txt', 'w') as tex:
    for nome, nota in alunos.items():
        tex.write(f'{nome},{nota}\n')

with open('/home/thiago/Documents/IA_Expert/Programacao em python/topico_34/grade.txt') as tex:
    for linhas in tex:
        print(linhas)

