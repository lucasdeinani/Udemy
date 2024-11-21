# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

# Salvar os dados
import json
from os import system

CAMINHO_ARQUIVO = 'aula127_meu.json'

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        #self.ano_nascimento = Pessoa.ano_atual - idade

def boas_vindas():
    return f'#########################\n' + \
    '#    CADASTRO PESSOA    #\n' + \
    '#########################'

def informar_dados():
    global dados_pessoa

    print()
    nome = input('Seu nome: ')
    sobrenome = input('Seu sobrenome: ')
    idade = input('Sua idade: ')

    dados_pessoa = Pessoa(nome=nome, sobrenome=sobrenome, idade=idade)
    return valida_dados_digitados()

def valida_dados_digitados():
    confirmar = 'falta'

    print()
    print('DADOS DIGITADOS: ')
    for pessoa in vars(dados_pessoa):
        print(pessoa.upper(), '-', dados_pessoa.__dict__[pessoa])
    
    print()
    while confirmar not in ('SIM', 'NÃO', 'NAO', 'S', 'N'):
        confirmar = input(
            'Os dados digitados estão corretos?\n' + \
            '(S)im/(N)ão\n'
            ).strip().upper()
    
    if confirmar[0] == 'S':
        return True
    
    system('cls')
    return informar_dados()

def salvar(dados, caminho_arquivo):
    dados_salvar = dados
    print(f'Cadastrando {dados_salvar.nome}...')

    with open(caminho_arquivo, 'w', encoding='UTF-8') as arquivo:
        dados_salvar = json.dump(vars(dados_salvar), arquivo, indent=2, ensure_ascii=False)
    return dados_salvar

dados_pessoa = None

if __name__ == '__main__':
    while True:
        print(boas_vindas())

        if informar_dados():
            salvar(dados_pessoa, CAMINHO_ARQUIVO)
        break