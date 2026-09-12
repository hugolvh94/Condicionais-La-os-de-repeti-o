produto = float(input('Digite o preço do produto: '))

if produto == 4490.99:
    print('Notebook R$: ', produto)

elif produto >= 3000 and produto <= 4000:
    print('Eletrodomestico R$: ', produto)

elif produto >= 5000:
    print('Smartphone R$: ', produto)

else:
    print('Produto não encontrado!')
