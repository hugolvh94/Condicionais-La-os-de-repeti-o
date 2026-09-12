numero1 = int(input('Insira um valor numérico: '))
numero2 = int(input('Insira um número: '))
operacao = input('Insira a operação desejada (+, -, *, /): ')

soma = numero1 + numero2
subtracao = numero1 - numero2
divisao = numero1 / numero2
multiplicacao = numero1 * numero2

if operacao == '+':
    print(f'A soma de {numero1} e {numero2} é: {soma}')
elif operacao == '-':
    print(f'A subtração de {numero1} e {numero2} é: {subtracao}')
elif operacao == '*':
    print(f'A multiplicação de {numero1} e {numero2} é: {multiplicacao}')
elif operacao == '/':
    if numero2 != 0:
        print(f'A divisão de {numero1} e {numero2} é: {divisao}')
else:
    print('Erro: Operação inválida.')

