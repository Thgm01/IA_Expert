from statistics import mean
nota = list()
for i in range(0, 5):
    nota.append(float(input(f'Informe a {i+1}° nota: ')))

media = mean(nota)


print(f'Sua média foi de {media:.2f}')