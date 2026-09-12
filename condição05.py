a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

x = b * c + 300/2 * a

print(x)

if x > 1000:
    print('O resultado é maior do que 1000!')
if x == 1000:
    print('O resultado é igual a 1000!')
if x < 1000:
    print('O resultado é menor do que 1000!')