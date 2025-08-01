import sqlite3
from main import DB_FILE, TABLE_NAME


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    # f'SELECT * FROM {TABLE_NAME} LIMIT 2'
    f'SELECT * FROM {TABLE_NAME} '
)

for row in cursor.fetchall(): # fetchall retorna o valor em questão para dentro da row.
    _id, name, weight = row
    print(f'ID: {_id}, Nome: {name}, Peso: {weight}')

print()

cursor.execute(
    # f'SELECT * FROM {TABLE_NAME} LIMIT 2'
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "3"'
)

row = cursor.fetchone()  # fetchone retorna o primeiro valor da consulta
# print(row)  # Exibe a tupla com os dados da primeira linha
_id, name, weight = row
print(_id, name, weight)

cursor.close()
connection.close()