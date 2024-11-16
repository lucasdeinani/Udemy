# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia', 
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliester'],
]

megasena = [i for i in range(1, 61)]

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
# print_iter(product(*camisetas))

# possibilidades = len(list(combinations(megasena, 6)))
# print(possibilidades)
