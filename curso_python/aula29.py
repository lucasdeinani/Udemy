"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

# print(1234)
# print(456)
# int('a')

numero_str = input('Vou dobrar o número que você digitar: ')

print(numero_str.isdigit())

#if numero_str.isdigit():
#   numero_float = float(numero_str)
#   print(f'O dobro de {numero_str} é {numero_str * 2:.2f}')
#else:
#   print('Isso não é um número')

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')