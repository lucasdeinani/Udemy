"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# Dunder dois __

# texto = 'Luiz'.__iter__() # mesma coisa que o de baixo
#texto = iter('Luiz')
#print(texto)

#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__()) # Irá gerar erro de StopIteration

#print(next(texto))
#print(next(texto))
#print(next(texto))
#print(next(texto))
#print(next(texto)) # Irá gerar erro de StopIteration

#numeros = range(0, 100, 8)

#for numero in numeros:
#    print(numero)

#for letra in texto:
texto = 'Luiz' # iterável
iterator = iter(texto) # iterador

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

#   IGUAl A

for letra in texto:
    print(letra)