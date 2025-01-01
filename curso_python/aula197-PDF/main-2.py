# PyPDF2 para manipular arquivos PDF (PdfReader)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/ # Não existe mais
# Link NOVO: https://pypdf.readthedocs.io/en/latest/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path

from pypdf import PdfReader, PdfWriter

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20241227.pdf'
# RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230210.pdf'
PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()

page0 = reader.pages[0]
imagem0 = page0.images[0]

# for imagem in page0.images:
#     print(imagem.name)

# print(page0.extract_text())
# print(page0.images[0])

# with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
#     fp.write(imagem0.data)

# para uma Página apenas
# writer = PdfWriter()
# writer.add_page(page0)

# with open(PASTA_NOVA / 'page0.pdf', 'wb') as arquivo:
#     writer.write(arquivo)

# para um arquivo PDF com todas as páginas juntas
writer = PdfWriter()

with open(PASTA_NOVA / 'page0.pdf', 'wb') as arquivo:
    for page in reader.pages:
        writer.add_page(page)

    writer.write(arquivo)

# para cada páginas em um PDF separado

for i, page in enumerate(reader.pages):
    writer = PdfWriter()

    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)
