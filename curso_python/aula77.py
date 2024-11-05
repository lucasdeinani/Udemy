# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acerto = 0
resposta_posicao = 0
quantidade_perguntas = len(perguntas[0])

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'], '\n')

    for indice, opcoes in enumerate(pergunta['Opções']):
        print(f'{indice}) {opcoes}')

        if pergunta['Resposta'] == opcoes:
            resposta_posicao = str(indice)

    escolha_usuario = input('Escolha uma opção: ')

    if escolha_usuario == resposta_posicao:
        print('Acertou 👍\n')
        acerto += 1
    else:
        print('Errou ❌\n')

print(f'Você acertou {acerto}\nde {quantidade_perguntas} perguntas.')
