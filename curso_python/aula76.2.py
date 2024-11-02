#Manipulando chaves e valores em dicionários
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ],
# }

pessoa = {}

#pessoa['nome'] = 'Luiz Otávio'

#print(pessoa)
#print(pessoa['nome'])

chave = 'nome_completo'
chave = 'nome'
pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

print(pessoa)
print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']

print(pessoa)
print(pessoa[chave])

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])