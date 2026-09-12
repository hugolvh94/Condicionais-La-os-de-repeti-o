automovel = int(input('Digite o ano do automóvel: '))


if automovel > 1990 and automovel <= 2000:
    print('Veículo usado!')

elif automovel > 2000 and automovel < 2010:
    print('Veículo Semi-novo!')

elif automovel >= 2010:
    print('Veículo Novo!')

else:
    print('Ano não encontrado!')