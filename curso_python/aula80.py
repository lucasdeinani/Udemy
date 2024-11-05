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
def busca_repredido_segunda_vez(procura_lista, procurar_numero, exclui_indice):
    for indice, numero in enumerate(procura_lista):
        if indice != exclui_indice:
            if numero == procurar_numero:
                return indice
    return None

lista_de_listas_de_inteiros = [
    #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    #[9, 1, 8, *9, 9, 7, 2, 1, 6, 8],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    #[1, 3, 2, *2, 8, 6, 5, 9, 6, 7],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    #[3, *8, 2, 8, 6, 7, 7, 3, 1, 9],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    #[4, 8, *8, 8, 5, 1, 10, 3, 1, 7],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    #[1, 3, 7, 2, *2, 1, 5, 1, 9, 9],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    #[10, 2, *2, 1, 3, 5, 10, 5, 10, 1],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    #[1, 6, *1, 5, 1, 1, 1, 4, 7, 3],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    #[1, 3, 7, *1, 10, 5, 9, 2, 5, 7],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    #[4, 7, 6, 5, 2, 9, *2, 1, 2, 1],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    #[5, 3, 1, 8, 5, 7, *1, 8, 8, 7],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

for lista in lista_de_listas_de_inteiros:
    segunda_ocorrencia = None
    posicao = None

    for indice, numero in enumerate(lista):
        if posicao is None:
            posicao = busca_repredido_segunda_vez(lista, numero, indice)
        else:
            segunda_ocorrencia = lista[posicao]
            break
    


    print('Nesta lista', lista)
    if posicao is not None:
        print(f'O primeiro número repedido é o {segunda_ocorrencia} na posição {posicao}.\n')
    else:
        print('Não há nenhum número repetido nesta lista.\n')

"""
lista_teste = [9, 1, 8, 9, 9, 7, 2, 1, 6, 8]
#  0  1  2    3    4  8  9  7  8  9
# [9, 1, 8, ->9<-, 9, 7, 2, 1, 6, 8]
primeira_ocorrencia = lista_teste[0]
segunda_ocorrencia = None
posicao = 0

for numero in lista_teste[1:]:
    posicao +=1

    if primeira_ocorrencia == numero:
        segunda_ocorrencia = numero
        break

print(f'O primeiro número repedido é o {segunda_ocorrencia} na posição {posicao}')
"""