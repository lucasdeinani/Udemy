"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf_inteiro = '015.507.900-05'

cpf_sem_formatacao = []

posicao_numeros_cpf = 0
soma = 0
digito_1_digitado = 0
digito_1_verificado = 0
digito_1 = 0

cpf_valido = True

for caracter in cpf_inteiro[-1::-1]:
    if caracter.isnumeric():
        cpf_sem_formatacao.append([posicao_numeros_cpf, int(caracter)])
        posicao_numeros_cpf += 1

for posicao, numero_cpf in cpf_sem_formatacao:
    soma += (posicao * numero_cpf)

print(soma)

digito_1_digitado = cpf_sem_formatacao[1][1]
digito_1 = (soma * 10) % 11
digito_1_verificado = 0 if digito_1 > 9 else digito_1

cpf_valido = True if digito_1_verificado == digito_1_digitado else False

print(digito_1_verificado)

