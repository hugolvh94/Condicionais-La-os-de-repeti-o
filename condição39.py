levitico = input('Como concatenar:')
print('Apelando para levítico')

resposta = input('E o que seria levítico?')

if resposta.lower() == "tem que concatenar":
    linguagem = input("Com quem?")
    print(f"Ótima escolha! Vamos aprender {linguagem}.")
else:
    motivo = input("Motivo:")
    print(f"Entendi. Motivo: {motivo}")