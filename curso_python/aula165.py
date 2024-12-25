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
    while data_ini <= data_fim:
        data_ini = adiciona_um_mes(data_ini)
        meses += 1
    return meses


emprestimo = 1000000.00
fmt = '%d/%m/%Y'
data_emprestimo = datetime.strptime('20/12/2020', fmt)
data = data_emprestimo
data_final_emprestimo = data_emprestimo + relativedelta(years=5)
