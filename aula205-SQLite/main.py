import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Create Read   Update Delete
# SQL -  INSERT SELECT UPDATE DELETE

# CUIDADO: fazendo delete sem where
# Pois não tem truncate table
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
connection.commit()

# Reseta sequencia do id
# DELETE mais cuidadoso
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores nas colunas da tabela
# CUIDADO: sql injection
# sql = (
#     f'INSERT INTO {TABLE_NAME} '
#     '(name, weight) '
#     # '(id, name, weight) '
#     'VALUES '
#     '("Helena", 4), '
#     '("Eduardo", 10)'
#     # '(NULL, "Helena", 4), '
#     # '(NULL, "Eduardo", 10)'
# )
# Ao invés disso
# fazer isso
# sql = (
#     f'INSERT INTO {TABLE_NAME} '
#     '(name, weight) '
#     'VALUES '
#     '(?, ?), '  # bindings, placeholders, etc
# )
# cursor.execute(sql, ['Joana', 4])
# Pode ser utilizado listas,
# porém é melhor tuplas pois você não irá mudar os valores
# cursor.executemany(sql, [['Joana', 4], ['Luiz', 5]])
# cursor.executemany(
#     sql,
#     (
#         ('Joana', 4), ('Luiz', 5)
#     )
# )

# Com dicionário
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:nome, :peso)'  # bindings, placeholders, etc
)
cursor.execute(sql, {'nome': 'Sem nome', 'peso': 3})
cursor.executemany(
    sql,
    (
        {'nome': 'Joãozinho', 'peso': 3},
        {'nome': 'Maria', 'peso': 2},
        {'nome': 'Helena', 'peso': 4},
        {'nome': 'Joana', 'peso': 5}
    )
)
connection.commit()


if __name__ == '__main__':
    print(sql)

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3"'
    )
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = 1'
    )
    connection.commit()

    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name="QUALQUER", weight=67.89 '
        'WHERE id = 2'
    )
    connection.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME} '
    )
    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    # Sempre finalizar as conexões
    cursor.close()
    connection.close()
