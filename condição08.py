pergunta = int(input('Digite a velcidade do automóvel: '))

print(pergunta)

if pergunta > 80:
    print('O usuário foi multado!')

multa = ((pergunta - 80) * 5) 

#print('O valor da multa é: R$ {:.2f}'.format(multa * 5))

print('O valor da multa é: R$', multa)