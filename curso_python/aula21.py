# Operadores lógicos 
# and (e) or (ou) not (não) 
# and - Todas as condições precisam ser 
# verdadeiras. 
# Se qualquer valor for considerado falso, 
# aexpressão inteira será avaliada naquele valor
# São considerados falsy (que você já viu) 
# 0 0.0 '' False 
# Tambémexiste o tipo None que é 
# usadao para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
print(True and True and True)
print(True and False and True)