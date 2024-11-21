# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

# Recuperar os dados
import json
from aula127_a import CAMINHO_ARQUIVO, Pessoa

with open(CAMINHO_ARQUIVO, 'r', encoding='UTF-8') as arquivo:
    pessoas = json.load(arquivo)
    
    for pessoa in pessoas:
        print(pessoa.upper(), '-', pessoas[pessoa])