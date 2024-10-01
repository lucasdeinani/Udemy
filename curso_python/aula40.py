""" Calculadora com while """

"""
    Minha formula de solução
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    operadores_permitidos = '+-/*'
    resultado = 0.0

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    try:
        numero_1_inteiro = int(numero_1)
        numero_2_inteiro = int(numero_2)

        if operador == '+':
            resultado = numero_1_inteiro + numero_2_inteiro
            print(f'A soma de {numero_1} com {numero_2} é {resultado:.2f}')
        elif operador == '-':
            resultado = numero_1_inteiro - numero_2_inteiro
            print(f'A soma de {numero_1} com {numero_2} é {resultado:.2f}')
        elif operador == '/':
            resultado = numero_1_inteiro / numero_2_inteiro
            print(f'A soma de {numero_1} com {numero_2} é {resultado:.2f}')
        else:
            resultado = numero_1_inteiro * numero_2_inteiro
            print(f'A soma de {numero_1} com {numero_2} é {resultado:.2f}')

    except:
        print('Você deve digitar números válidos!')
        continue
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair:
        break
"""

#    Solução professor
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numero_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numero_validos in None:
        print('um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui.')        
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair:
        break