# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
# C:\Users\Administrator\Desktop\Area de trabalho\FTEC\2024\
# Engenharia_de_Software_II
import os

CAMINHO = os.path.join(
    '\\Users', 'Administrator', 'Desktop', 'Area de trabalho', 'FTEC',
    '2024', 'Engenharia_de_Software_II'
)

for pasta in os.listdir(CAMINHO):
    caminho_completo_pasta = os.path.join(CAMINHO, pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue
    print(pasta)
    for imagem in os.listdir(caminho_completo_pasta):
        print('    ' + imagem)
