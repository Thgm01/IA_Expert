def ler_temp():
    temp = float(input('Insert the temperature in Celsius: '))
    return temp

def ctof(temp_cel):
    temp_fa = (9*temp_cel+160)/5
    return temp_fa

def print_f(temp_fa):
    print(f'The temperature em Fahrenheit é de {temp_fa}')

temp = ler_temp()
temp_n = ctof(temp)
print_f(temp_n)
