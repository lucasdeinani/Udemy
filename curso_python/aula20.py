primeiro_valor = input('Digitwe um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    mensagem = f'{primeiro_valor=} é maior do que {segundo_valor=}'
if primeiro_valor == segundo_valor:
    mensagem = 'Ambos valores são iguais'
else:
    mensagem = f'{segundo_valor=} é maior do que {primeiro_valor=}'

print(mensagem)
"""
Outra solução

int_primeiro_valor = primeiro_valor
int_segundo_valor = segundo_valor

if int_primeiro_valor > int_segundo_valor:
    mensagem = f'{primeiro_valor=} é maior do que {segundo_valor=}'
if primeiro_valor == segundo_valor:
    mensagem = 'Ambos valores são iguais'
else:
    mensagem = f'{segundo_valor=} é maior do que {primeiro_valor=}'

print(mensagem)
"""

