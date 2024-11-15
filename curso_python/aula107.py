# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

"""Forma inicial v2
def zipper(*args):
    nova_lista = []

    for item in range(len(args[0])):
        nova_lista.append((args[0][item], args[1][item]))
    return nova_lista
"""

def cria_funcao(func):
    def verifica_menor(*args):
        args = sorted(args, reverse=True)

        return func(*args)
    return verifica_menor

def zipper(*args):
    nova_lista = []

    for item in range(len(args[0])):
        nova_lista.append((args[0][item], args[1][item]))
    return nova_lista

lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_2 = ['BA', 'SP', 'MG', 'RJ']
lista_3 = []

lista_3 = cria_funcao(zipper)
lista_3 = lista_3(lista_2, lista_1)

print(*lista_3, sep='\n')

#Forma inicial v1
"""
if len(lista_1) < len(lista_2):
    menor = lista_1
    maior = lista_2
else:
    menor = lista_2
    maior = lista_1

for item in range(len(menor)):
    lista_3.append((menor[item], maior[item]))
"""
print(*lista_3, sep='\n')