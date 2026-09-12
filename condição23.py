a = int(input('Insira o valor de a: '))
b = int(input('Insira o valor de b: '))

operacao = input('Insira a operação desejada (+, -, *, /): ')

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b if b != 0 else 'Erro: Divisão por zero não é permitida.'

if operacao == '+':
    print(f'A soma de {a} e {b} é: {soma}')
elif operacao == '-':
    print(f'A subtração de {a} e {b} é: {subtracao}')
elif operacao == '*':
    print(f'A multiplicação de {a} e {b} é: {multiplicacao}')
elif operacao == '/':
    print(f'A divisão de {a} e {b} é: {divisao}')
