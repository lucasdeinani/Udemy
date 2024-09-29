"""
Repetições
while (enquanto)
Executa uma ação enquanto uma consição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

condicao = True

"""
while condicao: #Gera loop
    print(1)
    print(2)
    print(3)
"""

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')