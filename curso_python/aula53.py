"""
enumerate - enumera iteráveis (indices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# lista_enumerada = enumerate(lista)
# print(next(lista_enumerada))

for item in enumerate(lista):
    print(item)

lista_enumerada = list(enumerate(lista))
# lista_enumerada = list(enumerate(lista, start=19))
print(lista_enumerada)
for item in lista_enumerada:
    print(item)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

for indice, nome in enumerate(lista):
    print(indice, nome)