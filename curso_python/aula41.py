"""while/else"""

string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    print(letra)
    i += 1

    if letra == ' ':
        break
else:
    print('Não encontri um espaço na string.')

print('Fora do while.')