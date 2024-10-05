"""
Faça um jogo para o usuário adicinhar qual 
a palavra secreta.
- Você vai propor uma palavra secreta 
qualquer e vai dar a possibildiade para 
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está 
na palavra secreta.
    - Se a letra digitada estiver na 
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver 
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu 
usuário.
"""

#Meu teste de resolução do problema
"""
palavra_secreta = 'perfume'

while True:
    palavra_com_asteriscos = len(palavra_secreta) * '*'

    posicao = 0

    try:
        letra_digitada = input('Digite uma letra: ')

        letra_digitada = letra_digitada.lower()

        if len(letra_digitada) != 1:
            print('Digite apenas uma letra')
            continue
        
        for letra in palavra_secreta:
            if letra == letra_digitada:
                palavra_com_asteriscos[posicao] = letra
            print(palavra_com_asteriscos[posicao])
            posicao += 1

        print(palavra_com_asteriscos)

        if palavra_com_asteriscos.count('*') == 0:
            print('Você acertou a palavra!')
            break
    except:
        print('Não deveria cair aqui')
"""

import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palavra Formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0