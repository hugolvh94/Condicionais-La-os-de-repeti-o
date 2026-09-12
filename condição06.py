valor = int(input('Digite o preço do notebook: '))
desconto = valor * 30/100
valor_final = valor - desconto

print(valor_final)

if valor_final <= 3000:
    print('O notebook está em um valor promocional!')
if valor_final > 3000:
    print('O notebook não está em um valor promocional!')
