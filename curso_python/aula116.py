# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
# https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/

caminho_arquivo = 'C:\\Users\\Administrator\\Desktop\\Udemy\\Udemy\\curso_python\\'
# caminho_arquivo = r'C:\\Users\\Administrator\\Desktop\\Udemy\\Udemy\\curso_python\\'
# Pode-se utilizar o r na frente caso dê problemas com as barras invertidas
caminho_arquivo += 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     print(type(arquivo))
#     arquivo.write('Linha 1\n')
#     # arquivo.write('Linha 1\r\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n',)
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print('Lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline())
#     print('READLINES')
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())
# 
# print('#' * 10)
# 
# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

# with open(caminho_arquivo, 'a+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n',)
#     )

import os

with open(caminho_arquivo, 'w', encoding='UTF-8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n',)
    )

# os.remove(caminho_arquivo)
# Ambos fazem a mesma coisa
# os.unlink(caminho_arquivo)
# os.rename(caminho_arquivo, 'aula116-2.txt')