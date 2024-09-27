# Operadores lógicos 
# and (e) or (ou) not (não) 
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro, 
# a expressão inteira será avaliada naquele valor. 
# São considerados falsy (que você já viu) 
# 0 0.0 '' False 
# Tambémexiste o tipo None que é 
# usadao para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
print(True or True or True)
print(True or False or True)
print(0 or False or 0.0 or 'abc')

senha = input('Senha: ') or 'Sem senha'
print(senha)