# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

CAMINHO = os.path.join(
    '\\Users', 'Administrator', 'Desktop', 'Area de trabalho', 'FTEC',
    '2024', 'Engenharia_de_Software_II'
)
counter = count()

for root, dirs, files in os.walk(CAMINHO):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('    ', the_counter, 'Dir: ', dir_)

    for file_ in files:
        print('    ', the_counter, 'FILE: ', file_)
        # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
        # os.unlink(caminho_completo_arquivo)
