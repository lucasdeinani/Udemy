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
import json

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

    lista_tarefa.append(item.title())

    atualiza_lista_json(lista_tarefa)

def listar_lista(comando, lista):
    if not verifica_listas(comando, lista):
       return None

    print('\nLISTA:')
    for item in lista:
        print(item)

def remover_item_lista(comando, lista_remove, lista_adiciona):
    if not verifica_listas(comando, lista_remove):
        return None

    item = lista_remove.pop()
    lista_adiciona.append(item)

    if comando == 'desfazer':
        print(f'Foi removido o {item.upper()} da lista.')
        atualiza_lista_json(lista_remove)
    else:
        print(f'Foi adicionado o {item.upper()} a lista.')
        atualiza_lista_json(lista_adiciona)
    

def atualiza_lista_json(lista):
    with open('aula119_dict_json.json', 'w', encoding='UTF-8') as arquivo:
        json.dump(
            lista, 
            arquivo, 
            ensure_ascii=False, 
            indent=2,
        )

lista_tarefa = []
excluidos = []

while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ').lower()

    comandos = {
        'listar': lambda: listar_lista('listar', lista_tarefa),
        'desfazer': lambda: remover_item_lista('desfazer', lista_tarefa, excluidos),
        'refazer': lambda: remover_item_lista('refazer', excluidos, lista_tarefa),
        'clear': lambda: system('cls'),
        'exit': lambda: exit(0),
        'adicionar': lambda: adiciona_item_lista(tarefa),
    }

    comando = comandos.get(tarefa) \
            if comandos.get(tarefa) is not None \
            else comandos['adicionar']
    comando()
    print()