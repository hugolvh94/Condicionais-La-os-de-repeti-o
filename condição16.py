numero1 = int(input('Digite o valor de a: '))
numero2 = int(input('Digite o valor de b: '))
numero3 = int(input('Digite o valor de c: '))
if numero1 > numero2 and numero1 > numero3:
    print('O maior número é a: ', numero1)
elif numero2 > numero1 and numero2 > numero3:
    print('O maior número é b: ', numero2)
else:
    print('O maior número é c: ', numero3)
                        