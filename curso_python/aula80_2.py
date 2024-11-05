"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
def busca_repredido_segunda_vez(procura_lista, procurar_numero, indice_real):
    global primeira_segunda_aparicao

    for indice, numero in enumerate(procura_lista):
        if indice != 0 and numero == procurar_numero:
            primeira_segunda_aparicao.append(
                {
                    'Numero_primeiro': numero,
                    'Posicao_primeiro': indice_real,
                    'Numero_segundo': lista[indice+indice_real],
                    'Posicao_segundo': indice+indice_real,
                    'Distancia_numero_repetido': (indice + indice_real) - indice_real
                }
            )

            return True

def remove_repeticao_invalida(listas):
    global primeira_segunda_aparicao

    for indice, lista in enumerate(listas):
        if listas[0]['Posicao_segundo'] < lista['Posicao_primeiro']:
            del primeira_segunda_aparicao[indice]

def distancia_maior(listas):
    menor = listas[0]['Distancia_numero_repetido']

    for lista in listas:
        if menor > lista['Distancia_numero_repetido']:
            menor = lista['Distancia_numero_repetido']

    return menor   

lista_de_listas_de_inteiros = [
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

primeira_segunda_aparicao = None
mais_proximo = None

for indeice, lista in enumerate(lista_de_listas_de_inteiros):
    primeira_segunda_aparicao = []

    for indice, numero in enumerate(lista):
        busca_repredido_segunda_vez(lista[indice:], numero, indice)

    print('Na lista', lista_de_listas_de_inteiros[indeice])

    if len(primeira_segunda_aparicao):
        remove_repeticao_invalida(primeira_segunda_aparicao)
        mais_proximo = distancia_maior(primeira_segunda_aparicao)
    else:
        print('Não houve números duplicados.\n')


    for lista in primeira_segunda_aparicao:
        if lista['Distancia_numero_repetido'] == mais_proximo:
            print('O primeiro número repedido é o', lista['Numero_primeiro'])
            print('Na posição', lista['Posicao_segundo'] , 'da lista.\n')
    break