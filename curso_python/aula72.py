# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicacao(*args):
    total = args[0]
    
    for numero in args[1:]:
        total *= numero
    return total

variavel = 1, 2, 3, 4, 5
print(multiplicacao(*variavel))

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    if numero % 2 == 0:
        return 'PAR'
    return 'ÍMPAR'

#def par_impar(numero): #Solução professor
#    multiplo_de_dois = numero % 2 == 0
#
#    if multiplo_de_dois:
#        return f'{numero} é par'
#    return f'{numero} é ímpar'

variavel = 12
print('O número digitado é', par_impar(variavel))