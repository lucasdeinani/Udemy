import json
from aula127_a_professor import CAMINHO_ARQUIVO, Pessoa

with open(CAMINHO_ARQUIVO, 'r', encoding='UTF-8') as arquivo:
    pessoas = json.load(arquivo)
    
    for pessoa in pessoas:
        print(pessoa['nome'], pessoa['idade'])


