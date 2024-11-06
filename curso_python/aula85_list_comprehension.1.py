def divisaoFuncion(x, y):
    return x / y

def multiplicacaoFuncion(x, y):
    return x * y

def potenciacaoFuncion(x, y):
    return x ** y

numeros = [1, 2, 3, 4, 5]
divisao = [divisaoFuncion(numero, 2) for numero in numeros]
multiplicacao = [multiplicacaoFuncion(numero, 2) for numero in numeros]
potenciacao = [potenciacaoFuncion(numero, 2) for numero in numeros]

print(numeros)
print(divisao)
print(multiplicacao)
print(potenciacao)