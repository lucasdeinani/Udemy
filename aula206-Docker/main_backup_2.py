# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os
from typing import cast

import dotenv
import pymysql
import pymysql.cursors

TABLE_NAME = 'customers'
CURRENT_CURSOR = pymysql.cursors.SSDictCursor

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=CURRENT_CURSOR,
    # cursorclass=pymysql.cursors.SSDictCursor,  # Para consultas unbuffer
    # (sem salvar em memória), para clientes lentos ou conexões lentas.
    # Contra, não consegue saber a quantidade de linhas
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
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES (%s, %s) '
        )
        data = ('Luiz', 18)
        result = cursor.execute(sql, data)
        # print(sql, data)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES (%(name)s, %(age)s) '
        )
        # data = ('Luiz', 18)
        data2 = {
            "name": "Le",
            "age": 27
        }
        result = cursor.execute(sql, data2)
        # print(sql, data2)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES (%(name)s, %(age)s) '
        )
        # data = ('Luiz', 18)
        data3 = (
            {"name": "Sah", "age": 33, },
            {"name": "Júlua", "age": 74, },
            {"name": "Rose", "age": 53, },
        )
        result = cursor.executemany(sql, data3)  # type: ignore
        # print(sql, data3)
        # print(result)
    connection.commit()

    # Inserindo vários valores usando placeholder e uma tupla de tuplas
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES (%s, %s) '
        )
        # data = ('Luiz', 18)
        data4 = (
            ("Siri", 22, ),
            ("Helena", 15, ),
            ("Luiz", 18, ),
        )
        result = cursor.executemany(sql, data4)  # type: ignore
        # print(sql)
        # print(data4)
        # print(result)
    connection.commit()

    # Lendo os valores com SELECT
    with connection.cursor() as cursor:
        # menor_id = int(input('Digite o menor id: '))
        # maior_id = int(input('Digite o maior id: '))
        menor_id = 2
        maior_id = 4
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            # 'WHERE id >= %s AND id <= %s '
            'WHERE id BETWEEN %s AND %s '
        )
        cursor.execute(sql, (menor_id, maior_id))
        # Cuidar sql injection
        # print(cursor.mogrify(sql, (menor_id, maior_id)))
        data5 = cursor.fetchall()

        # for row in data5:
        #     print(row)

    # Deletando valores com DELETE, WHERe e placeholders no PyMySQL
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s '
        )
        cursor.execute(sql, (1,))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
        data6 = cursor.fetchall()

        # for row in data6:
        #     print(row)

    # Atualizando valores com UPDATE, WHERe e placeholders no PyMySQL
    with connection.cursor() as cursor:
        cursor = cast(CURRENT_CURSOR, cursor)

        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome = %s, idade = %s '
            'WHERE id = %s '
        )
        cursor.execute(sql, ('Eleonor', 102, 4))
        # Tem que ter esse commit para salvar os ajustes em banco efetivamente
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
        # data7 = cursor.fetchall()

        # for row in cursor.fetchall():
        #     _id, name, age = row
        #     print(_id, name, age)

        # for row in cursor.fetchall():
        #     _id, name, age = row.items()
        #     print(_id, name, age)

        # data7 = cursor.fetchall()

        # print()
        # print('For 1: ')
        # for row in data7:
        #     print(row)

        # print()
        # print('For 2: ')
        # for row in data7:
        #     print(row)

        # print()
        # print('For 1: ')
        # for row in cursor.fetchall():
        #     print(row)

        # print()
        # print('For 2: ')
        # cursor.scroll(-2)  # Relative
        # cursor.scroll(0, 'absolute')
        # for row in cursor.fetchall():
        #     print(row)

        # Utilizando isso cursor.fetchall(), tu consegue não copiar
        # para uma variável inumeros dados, para não deixar lento, podendo
        # carregar x nº de registros e depois setar o cursor para os
        # próximos x nº de registros

        # Ao utilizar o SSDictCursor deve-se utilizar fetchall_unbuffered()
        print()
        print('For 1: ')
        for row in cursor.fetchall_unbuffered():
            print(row)

            if row['id'] >= 5:
                break

        print()
        print('For 2: ')
        # cursor.scroll(-1)  # Dará erro - Ele nunca volta
        # cursor.scroll(1)  # Não dará erro
        for row in cursor.fetchall_unbuffered():
            print(row)
