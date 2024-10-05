"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamentos
Métodos útei:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - 
Create Read Update   Delete
Criar, ler, alterar, apagar = lista [i] (CRUD)
"""

lista = [10, 20, 30, 40]
lista.append('Luiz')
print(lista)
nome = lista.pop()
print(lista, nome)
lista.append(1233)
del lista[-1]
print(lista)
#lista.clear()
lista.insert(0, 5)
print(lista)