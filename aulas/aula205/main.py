import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor() # Vai executar as consultas, criar, eliminar as coisas dentro do banco de dados

# CRUD - Create, Read, Update, Delete
# SQL - INSERT, SELECT, UPDATE, DELETE

# CUIDADO: fazendo delete sem where (Limpar Tabela)
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
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
sql = (
    f'INSERT INTO {TABLE_NAME}' 
    '(name, weight)'
    'VALUES'
    '(:nome, :peso)'
)

# Os possíveis nomes do ? são: bindings, placeholders, parâmetros e outros.

# cursor.execute(sql, ['Joana', 4])
# cursor.executemany(
#     sql, 
#     (
#         ('Joana', 4), ('Luiz', 5)
#     )
# )
cursor.execute(sql, {'nome':'Sem nome', 'peso': 3})
cursor.executemany(sql, (
        {'nome':'Maria', 'peso': 3},
        {'nome':'Helena', 'peso': 2},
        {'nome':'João', 'peso': 6},
        {'nome':'Rafa', 'peso': 5},
))
connection.commit()

if __name__ == '__main__':
    print(sql)

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3"'
    )

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "1"'
    )

    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name = "QUALQUER", weight=67.89 '
        'WHERE id = "2"'
    )

    connection.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME} '
    )

    for row in cursor.fetchall():
        _id, name, weight = row
        print(f'ID: {_id}, Nome: {name}, Peso: {weight}')

    cursor.close()
    connection.close()