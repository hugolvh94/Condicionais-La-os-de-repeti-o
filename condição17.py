plano = input('Qual o seu plano de celular: ')
if plano == 'controle':
    print('Minutos no plano: 100')
    print('Valor do minuto extra: R$ 0,20')
if plano == 'pós-pago':
    print('Minutos no plano: 200')
    print('Valor do minuto extra: R$ 0,10')
    print('Preço do plano: R$ 80')
else:
    print('Plano inválido')
    exit()