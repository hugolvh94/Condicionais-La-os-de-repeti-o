nome = 'VH94PYTHON'
senha = '20099*'
entrada = input('Digite seu nome: ')
entrada_senha = input('Digite sua senha: ')

if entrada == nome and entrada_senha == senha:
    print('Acesso permitido!')
elif entrada != nome and entrada_senha == senha:
    print('Acesso negado! Nome incorreto!')
elif entrada == nome and entrada_senha != senha:
    print('Acesso negado! Senha incorreta!')
else:
    print('Acesso negado! Nome e senha incorretos!')    