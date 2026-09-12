taxi = float(input('Kilometros percorridos pelo taxi: '))
km = 4.50
tarifa = taxi * km * 1.25

if taxi > 100:
    print('Valor da tarifa: ', tarifa)
elif taxi >= 50 and taxi <=100:
    print('Valor da tarifa: ', tarifa)
elif taxi < 50 and taxi > 20:
    print('A corrida saiu de graça!')