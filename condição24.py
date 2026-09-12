animais = 'cavalo'
animais1 = 'águia'
animais2 = 'peixe'
animais3 = 'macaco'

animal = input('Insira o nome de um animal: ')

if animal == 'cavalo':
    print(f'O animal {animal} é um mamífero.')
elif animal == 'águia':
    print(f'O animal {animal} é uma ave.')
elif animal == 'tubarão':
    print(f'O animal {animal} é um peixe.')
elif animal == 'macaco':
    print(f'O animal {animal} é um mamífero.')
else:
    print('Animal não reconhecido.')