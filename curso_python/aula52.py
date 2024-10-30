"""
Tipo tupla - Uma lista imutável
"""
nomes = 'Maria', 'Helena', 'Luiz'
nomes = ('Maria', 'Helena', 'Luiz')
nomes = ['Maria', 'Helena', 'Luiz']
nomes = tuple(nomes)
nomes = list(nomes)

# nomes[1] = 'outro' # Gera erro TypeError
print(nomes[0])
print(nomes)