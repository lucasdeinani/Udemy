# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
import copy

from dados import produtos, ordena

novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.10, 2)}
    for produto in copy.deepcopy(produtos)
]

produtos_ordenados_por_nome = ordena(copy.deepcopy(produtos), 'nome', True)

produtos_ordenados_por_preco = ordena(copy.deepcopy(produtos), 'preco')

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')