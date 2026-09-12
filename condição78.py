L = [1, 8, 21, 12, 3, 90, 205,800, 73]
p = int(input('Digite o valor a procurar:'))
achou = False
x = 0
while x < len(L):
    if L[x] == p:
        achou = True
        break
    x += 1
if achou:
        print(f'{p} achado na posição {x}')
else:
        print(f'{p} não encontrado')