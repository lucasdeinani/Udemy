"""
Fatiamento de strings
  0 1 2 3 4 5 6 7 8
  O l á   m u n d o
 -9-8-7-6-5-4-3-2-1
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a
quantidade de caracteres da string
"""

variavel = 'Olá mundo'
print(variavel[-4])
print(variavel[4:])
print(variavel[4:8])
print(variavel[:5])
print(variavel[-8:-2])
print(len(variavel[3]))
print(len(variavel))
print(variavel[0:9:1])
print(variavel[0:9:2])
print(variavel[-1::-1])
print(variavel[-1:-10:-1])
print(variavel[::-1])
print(variavel[::-2])