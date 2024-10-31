"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = 'Olha só que, coisa interesante'
lista_palavras = frase.split()
print(lista_palavras)
lista_frases = frase.split(', ')
print(lista_frases)

lista_frases_1 = frase.split(',')

for i, frase in enumerate(lista_frases_1):
    lista_frases_1[i] = lista_frases_1[i].strip() #rstrip() ou lstrip()

print(lista_frases_1)

frase = 'Olha só que, coisa interesante'
lista_frases_cruas = frase.split(',')
lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases)

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)