tempo_de_viagem = float(input('Tempo gasto de viagem (h): '))
velocidade_media = float(input('Velocidade média (km/h): '))

distancia = tempo_de_viagem * velocidade_media
litros_usados = distancia/12

print(f"Para uma viagem de {tempo_de_viagem} horas a uma velocidade de {velocidade_media} km/h, a distância percorrida será de {distancia} km\n** Será necessário {round(litros_usados,1)} litros de gasolina **")
