"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

#def soma(x, y):
#    return x + y

#print(1)
#print(1, 2, 3, 4, 5)

#def soma(*args):
#    #print(args, type(args))
#    total = 0
#    for numero in args:
#        print('Total', total, '+', numero)
#        total += numero
#        print('Total', total)
#    print(total)

def soma(*args):
    #print(args, type(args))
    total = 0
    for numero in args:
        total += numero
    return total

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)

numero = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numero)
print(outra_soma)

print(sum((1, 2, 3, 4, 5, 6, 7, 78, 10)))
print(sum(numero))