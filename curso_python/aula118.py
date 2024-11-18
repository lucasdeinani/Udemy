# Problemas dos parâmetros mutáveis em funções Python
# def adiciona_clientes(nome, lista=[]): #é um parâmetro mutável uma lista
#     lista.append(nome)
#     return lista
# 
# lista1 = []
# cliente1 = adiciona_clientes('luiz', lista1)
# adiciona_clientes('Joana', cliente1)
# print(cliente1)
# 
# cliente2 = adiciona_clientes('Helena')
# adiciona_clientes('Maria', cliente2)
# print(cliente2)

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)