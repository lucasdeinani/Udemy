# Operadores lógicos 
# and (e) or (ou) not (não) 
# not - Usado para invertes 
# expressões 
# not True = False
# not False = True

senha = input('Senha: ')

if senha != '123456':
    print('Senha incorreta.')

if not senha:
    print('Você não digitou nada')

print(not True)
print(not 0)
print(not 1)