"""
Iterando strings com while
"""
"""
#       012345678910
nome = 'Luiz Otávio' # Iterávios

tamanho_nome = len(nome)
print(nome)
"""

nome = input('Digite seu nome: ')
caracter = input('Informe qual caracter quer\nentre as letras de seu nome: ')
tamanho_nome = len(nome)
contador = 0
unir_nome_caracter = ''

while contador < tamanho_nome:
    unir_nome_caracter += caracter + nome[contador]
    # unir_nome_caracter += f'{caracter}{nome[contador]}'
    contador += 1
    
    if contador == tamanho_nome:
        unir_nome_caracter += caracter
        # unir_nome_caracter += f'{caracter}'

print(unir_nome_caracter)