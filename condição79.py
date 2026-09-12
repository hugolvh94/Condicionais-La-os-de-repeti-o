L = [2, 4, 6, 8, 10, 20]
p = int(input('Digite o valor a procurar:'))
condicao = False
x = 0
while x < len(L):
    if L[x] == p:
        condicao = True
        break
    x += 1
if condicao:
    print(f'{p} achado na posição {x}')
else:
    print(f'{p} não encontrado')