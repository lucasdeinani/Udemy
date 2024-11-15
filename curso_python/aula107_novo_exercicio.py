# Considerando duas listas de inteiros ou floats (lista A e lista B)
# Some os valores nas listas retornando uma nova lista com os valores somados:
# Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
# menor.
# Exemplo:
# lista_a     = [1, 2, 3, 4, 5, 6, 7]
# lista_b     = [1, 2, 3, 4]
# =================== resultado
# lista_soma  = [2, 4, 6, 8]
from itertools import zip_longest

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_c = [
    sum(x)
    for x in zip(lista_a, lista_b)
]

lista_d = [
    sum(x)
    for x in zip_longest(lista_a, lista_b, fillvalue=0)
]

lista_e = [
    lista_a[x] + lista_b[x]
    for x in range(min(len(lista_a), len(lista_b)))
]

def soma_listas(*args, lista):
    minimo = min(len(lista_a), len(lista_b))

    for x in range(minimo):
        lista.append(args[0][x] + args[1][x])
    return None

lista_f = []
soma_listas(lista_a, lista_b, lista=lista_f)

lista_g = [
    x + y
    for x, y in zip_longest(lista_a, lista_b, fillvalue=0)
]

lista_h = [
    sum((x, y))
    for x, y in zip_longest(lista_a, lista_b, fillvalue=0)
]

print(lista_c)
print(lista_d)
print(lista_e)
print(lista_f)
print(lista_g)
print(lista_h)