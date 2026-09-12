mercado = int(input('Digite o valor do Café: '))
mercado1 = int(input('Digite o valor do queijo: '))
mercado2 = int(input('Digite o valor do Refrigerante: '))
compra = mercado + mercado1 + mercado2
desconto = compra * 15/100
total= compra - desconto
print('Valor total da compra: ', compra)
print('Desconto aplicado: ', desconto) 
print('Total da compra: ', total)

if total <= 100:
    estacionamento = input('Esta fazendo uso de Estacionamento? ')
if estacionamento == 'Sim':
    print('Compra com desconto aprovada!')
if estacionamento == 'Não':
    print('Preço total da compra: ', compra)
