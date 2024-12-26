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


def adiciona_um_mes(data: datetime) -> datetime:
    data = data + relativedelta(months=1)
    return data


def conta_meses(data_ini: datetime, data_fim: datetime) -> int:
    meses = 0
    while data_ini < data_fim:
        data_ini = adiciona_um_mes(data_ini)
        meses += 1
    return meses


def mostra_vencimento_valor(
    data_ini: datetime,
    data_fim: datetime,
    emprestimo: float
) -> None:
    fmt = '%d/%m/%Y'
    meses = 0
    data = data_ini
    valor_parcela: float = 0.0

    while data < data_fim:
        data = adiciona_um_mes(data)
        meses += 1

    valor_parcela = emprestimo / meses

    meses = 0
    data = data_ini
    while data < data_fim:
        data = adiciona_um_mes(data)
        meses += 1
        print(
            '------\n'
            f'{meses}ª PARCELA\n'
            f'Vencimento: {data.strftime(fmt)}\n'
            f'Valor: R${valor_parcela:.2f}'
        )


emprestimo = 1000000.00
fmt = '%d/%m/%Y'
data_emprestimo = datetime.strptime('20/12/2020', fmt)
data_final_emprestimo = data_emprestimo + relativedelta(years=5)
mostra_vencimento_valor(data_emprestimo, data_final_emprestimo, emprestimo)
