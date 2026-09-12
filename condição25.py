a = int(input('Insira o valor da a:'))
b = int(input('Insira o valor da b:'))


operacao = input('Insira a operacao (+, *, -, /):')

if operacao == '+':
    print('O valor da operação entre a e b é de: ', a + b)
elif operacao == '*':
    print('O valor da operação entre a e b é de: ', a * b)
elif operacao == '-':
    print('O valor da operação entre a e b é de: ', a - b)
elif operacao == '/':
    print('O valor da operação entre a e b é de: ', a / b)
else:
    print('Erro!')
