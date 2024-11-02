"""
Retorno de valores das funções (return)
"""
def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y
    print(1+1) #unreachable

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1 + soma2)
print(soma1)
print(soma2)
print(soma(11, 55))

#variavel = soma(1, 2)
#variavel = int('1')
#print(variavel)

"""
print('Luiz')
variavel = print('Luiz')
#variavel = None
print(variavel)
print(variavel is None)
"""