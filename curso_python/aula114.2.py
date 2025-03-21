# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
# def recursiva(inicio=0, fim=10):
#     # Caso recursivo
#     # contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)
# 
# recursiva() # RecursionError: maximum recursion depth exceeded
# Também chamado de Stack Overflow
# Por causa da Call Stack, que está colocando muitas Call Stack
# Excedendo o limite máximo
# import sys
# sys.setrecursionlimit(1004) # Para ajustar o limite recursivo
# 
# def recursiva(inicio=0, fim=10):
#     
#     print(inicio, fim)
# 
#     # Caso base
#     if inicio >= fim:
#         return fim
# 
#     # Caso recursivo
#     # contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)
# 
# print(recursiva(0, 1000)) # Dá erro pois o limite o Python é 1 mil (1000)


def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(10))
print(factorial(12))
print(factorial(999))