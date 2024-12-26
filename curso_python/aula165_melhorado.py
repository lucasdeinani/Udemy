# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta


def adiciona_datas_entre_periodos(
    data_ini: datetime,
    data_fim: datetime,
    lista: list[datetime]
) -> None:
    while data_ini < data_fim:
        data_ini += relativedelta(months=1)
        lista.append(data_ini)


def mostra_parcelas_datas_valor(
    emprestimo: float,
    datas_parcelas: list[datetime],
    formato: str,
    valor_parcela: float
):
    mes = 0
    print(f'Foi solicitado um empréstimo de R${emprestimo:,.2f}')
    for data in datas_parcelas:
        mes += 1
        print(
            '---------------------\n'
            f'{mes}ª PARCELA\n'
            f'Vencimento: {data.strftime(formato)}\n'
            f'Valor: R${valor_parcela:,.2f}'
        )


emprestimo = 1_000_000.00
formato = '%d/%m/%Y'
data_emprestimo = datetime.strptime('20/12/2020', formato)
delta_anos = relativedelta(years=5)
data_final_emprestimo = data_emprestimo + delta_anos
datas_parcelas: list[datetime] = []

adiciona_datas_entre_periodos(
    data_emprestimo,
    data_final_emprestimo,
    datas_parcelas
)

quantidade_meses = len(datas_parcelas)
valor_parcela = emprestimo / quantidade_meses

mostra_parcelas_datas_valor(emprestimo, datas_parcelas, formato, valor_parcela)
