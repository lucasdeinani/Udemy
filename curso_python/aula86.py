# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
}
dc = {
    chave: valor * 1.05
    if isinstance(valor, (int, float)) else valor.upper() # Dá margem para erros de valores bool
    for chave, valor in produto.items()
}
dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]
dc = {
    chave: valor
    for chave, valor in lista
}
print(dc)
print(dict(lista))

# Set Comprehension
s1 = {2 ** i for i in range(10)}
print(s1)