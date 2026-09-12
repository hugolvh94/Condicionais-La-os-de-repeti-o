L = [7, 9, 10, 12]
p = int(input('Digite um número a pesquisar:'))
for e in L:
    if e == p:
        print(f'{p} encontrado na lista')
        break
else:
    print(f'{p} não encontrado na lista')