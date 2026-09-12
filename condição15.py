passageiro = int(input('Quantos Km deseja percorrer? '))

mensagem = passageiro * 0.50
mensagem1 = passageiro * 0.45

if passageiro <= 200:

    print('O valor da passagem é de R$', mensagem)

else: 
    print('O valor da passagem é de R$', mensagem1)
    