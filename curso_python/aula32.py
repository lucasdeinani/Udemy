"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
"""
numero_digitado = input('Digite um número inteiro: ')

try:
    numero_inteiro = int(numero_digitado)
    par_impar = numero_inteiro % 2 == 0

    if par_impar:
        print(f'O número {numero_digitado} é par.')
    else:
        print(f'O número {numero_digitado} é ímpar.')
except:
    print('O número digitado não é um inteiro.')
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
"""
pergunta_horario = input('Digite um horário inteiro (24h): ')

try:
    horario_inteiro = int(pergunta_horario)
    bom_dia = horario_inteiro in range(0,12)
    boa_tarde = horario_inteiro in range(12,18)

    if bom_dia:
        print('Bom dia!')
    elif boa_tarde:
        print('Boa tarde!')
    elif horario_inteiro > 23:
        print('Isto não é um horario válido!')
    else:
        print('Boa noite!')
except:
    print('Into não é um horário')
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input('Digite seu primeiro nome: ')
nome_curto = len(primeiro_nome) <= 4 
nome_normal = len(primeiro_nome) <= 6 and not nome_curto
nome_grande = len(primeiro_nome) > 6

if nome_curto:
    print('Seu nome é curto')
elif nome_normal:
    print('Seu nome é normal')
elif nome_grande:
    print('Seu nome é muito grande')
else:
    print('Ops, não deveria parar aqui')