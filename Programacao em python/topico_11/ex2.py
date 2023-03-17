from statistics import mean

n1 = float(input('Digite a nota M1: '))
n2 = float(input('Digite a nota M2: '))
n3 = float(input('Digite a nota M3: '))

media = mean([n1,n2,n3])

if media <= 4.0:
    print('Reprovado!')
elif media <= 6.0:
    print('Exame!')
    n4 = float(input('Digite a nota do Exame: '))
    if n4 > 6:
        print('Aprovado')
    else: 
        print('Reprovado')
else:
    print('Aprovado!')