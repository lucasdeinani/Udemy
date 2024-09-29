"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'luiz otávio'
outra_variavel = f'{string[:3]}ABC{string[4:]}'

print(f'{string=}')
print(f'{outra_variavel=}')
print(string.capitalize())
print(string.title())
print(string.zfill(20))
