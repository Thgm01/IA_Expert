lista = [0,0]
try:
    valor1 = float(input('Insert the first number: '))
    valor2 = float(input('Insert the second number: '))
    lista[0] = valor1
    lista[1] = valor2
    res = lista[0]/lista[1]
except ValueError:
    print('Incorrect type of variable, please insert a number: ')
except ZeroDivisionError:
    print("The second number can't be 0!")
except IndexError:
    print('this position do not exist in this list')
except KeyboardInterrupt:
    print('Interrution of program!')