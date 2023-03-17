idade = int(input("Digite sua idade: "))
if idade < 0:
    print("Idade Inválida")
elif idade < 13:
    print('Criança')
elif idade < 18:
    print('adolescente')
else:
    print('Adulto')