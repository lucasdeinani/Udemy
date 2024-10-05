"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamentos
Métodos útei:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista [i] (CRUD)
"""
"""
#         01234
#        -54321
string = 'ABCDE' # 5 caracteres
#print(bool(lista))
#print(lista, type(lista))

#        0    1     2               3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otáveio', 1.2, []] # ou list() -> menos comum
lista[-3] = 'Maria'
print(lista[2], type(lista[2]))
"""
lista = [10, 20, 30, 40]
numero = lista[2]
lista[2] = 300
print(lista[2], numero)
del lista[2]
print(lista, lista[2])

# Na lista é interessante sempre remover ou adicionar ao final, 
# pois o tempo de processamente para alterar os índices pode 
# deixar o sistema lento