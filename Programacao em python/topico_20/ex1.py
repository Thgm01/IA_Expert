lista = list()
for i in range(5):
    num = int(input(f'Insert your {i+1}° number: '))
    lista.append(num)

soma = 0
for i in lista:
    soma += i

print(f'The sum of this 5 numbers is {soma}')