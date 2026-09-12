x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))
z = int(input('Digite o valor de z: '))

equacao = (x + y) * z / 2 * y - z

print('O resultado da equação é: ', equacao)

if equacao > 1000:
    print('A equação é maior do que 1000!')
if equacao < 1000:
    print('A equação é menor do que 1000!')
if equacao == 1000:
    print('A equação é igual a 1000!')