idade = int(input('Digite a idade do usuário: '))
if idade < 16:
    print('O usuário não pode votar!')
if idade >= 16 and idade < 18:
    print('O voto é opcional!')
if idade >=18 and idade < 65:
    print('O voto é obrigatório!')
if idade >= 65:
    print('O voto é opcional!')
    