# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
import string
import locale
from datetime import datetime
from pathlib import Path


CAMINHO_ARQUIVO = Path(__file__).parent / 'aula183.txt'

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
    return brl


data = datetime(2022, 12, 28)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)

# print(json.dumps(dados, indent=2, ensure_ascii=False))

# template = string.Template(texto)
# Professor prefere esta pois garante que não vai enviar nada de errado
# KeyError: 'telefone'
# print(template.substitute(dados))
# Caso não tenha uma variávl no texto ela não dará erro
# e mostrará a variável no texto
# print(template.safe_substitute(dados))


class MyTemplate(string.Template):
    delimiter = '%'


with open(CAMINHO_ARQUIVO, 'r', encoding='UTF-8') as arquivo:
    texto = arquivo.read()
    template = MyTemplate(texto)
    # template = string.Template(texto)
    print(template.substitute(dados))
