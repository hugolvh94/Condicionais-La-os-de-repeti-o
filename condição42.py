valores = float(input('Nota de matemática: '))

valores2 = float(input('Nota de português: '))

valores3 = float(input('Nota de Física: '))

valores4 = float(input('Nota de Química: '))

media = (valores + valores2 + valores3 + valores4) / 4

print(f'A média das notas é: {media}')

if media >= 7:
    print('Você foi aprovado')
if media > 0 and media < 7:
    print('Aluno em recuperação')
if media == 0:
    print('Aluno reprovado')