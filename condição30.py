print('Um carro sai do ponto a as 17h 30min em uma velocidade de 10km/h, e passa ao ponto b as 17h 40min com uma velocidade de 410km/h. calcule sua velocidade média.')

delta_s = float(input('Insira o valor de Delta S:'))
delta_t = float(input('Insira o valor de Delta T:'))

metros = delta_s * 3.6

velocidade = metros / delta_t

print('O valor da velocidade é:', velocidade)