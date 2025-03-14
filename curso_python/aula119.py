# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
# https://en.wikipedia.org/wiki/Rubber_duck_debugging
# https://rubberduckdebugging.com
# https://pt.wikipedia.org/wiki/Debug_com_Pato_de_Borracha

"""
Deve apresentar a mensagem:
Comandos: listar, desfazer, refazer
Digite uma tarefa ou comando:

Um extra seria ter o comando *clear oculto onde limpa a tela do terminal
Quem sabe um exit
"""
from sys import exit
from os import system

def verifica_listas(comando, lista):
    if len(lista) > 0:
        return True
    print(f'Sem dados para {comando}.\n')
    return False

def adiciona_item_lista(item):
    item = item.strip()

    if not item:
        print('Você não digitou nada')
        return

    lista_tarefa.append(item)

def listar_lista(lista):
    if not verifica_listas(lista):
        print('\nLISTA:')
        for item in lista:
            print(item)

def remover_item_lista(lista_remove, lista_adiciona, item_removido_principal=None):
    item = lista_remove.pop()
    lista_adiciona.append(item)

    if item_removido_principal:
        print(f'Foi removido o {item.upper()} da lista.')
    else:
        print(f'Foi adicionado o {item.upper()} a lista.')

lista_tarefa = []
excluidos = []

while True:
    print('Comandos: listar, desfazer, refazer')
    comando = input('Digite uma tarefa ou comando: ').lower()

    if comando == 'listar':
        if verifica_listas(comando, lista_tarefa):
            listar_lista(lista_tarefa)
    elif comando == 'desfazer':
        if verifica_listas(comando, lista_tarefa):
            remover_item_lista(lista_tarefa, excluidos, 'sim')
    elif comando == 'refazer':
        if verifica_listas(comando, excluidos):
            remover_item_lista(excluidos, lista_tarefa)
    elif comando == 'clear':
        system('cls')
        pass
    elif comando == 'exit':
        exit(0)
    else:
        adiciona_item_lista(comando.title())

    print()