# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome=}')
#coloca nome= para saber o nome da variavel + retorno

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
# nunca utilizar a conversão de variáveis assim, 
# pois se o usuário digitar algo diferente do
# esperado, irá quebrar o programa
# numero_1 = int(input('Digite um número: '))
# numero_2 = int(input('Digite outro número: '))

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos número é: {int_numero_1 + int_numero_2}')