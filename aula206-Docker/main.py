# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os

import dotenv
import pymysql

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4'
)
# Como tanto o connectio quanto o cursor são Context Manager,
# ou seja, podemos utilizar with para abrir e fechar conexões
# cursor = connection.cursor()
# cursor.close()
# connection.close()

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ( '
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id) '
            ') '
        )
        # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME} ')
        # Possui alguns comandos, tal como, CREATE que não precisa do commit,
        # ou seja, não tem volta. Já com o commit() ele comita depois
        # connection.commit()
    connection.commit()

    # Começo a manipular dados a partir daqui

    with connection.cursor() as cursor:
        result = cursor.execute(
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES ("Luiz", 25) '
        )
        print(result)
    connection.commit()
