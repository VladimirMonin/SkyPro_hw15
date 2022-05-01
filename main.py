import sqlite3
from constants import OLD_DATABASE, CREATE_QUERIES, MIGRATE_SECOND, MIGRATE_JOIN


def get_sqlite_query(query, base=OLD_DATABASE, is_script=False):
    """Читаем старую базу данных"""
    with sqlite3.connect(base) as connection:
        cursor = connection.cursor()
        if is_script:
            cursor.executescript(query)
        else:
            cursor.execute(query)


# Создание новых таблиц. Основная таблица + допы
get_sqlite_query(CREATE_QUERIES, is_script=True)

# Заполнение доп. таблиц данными
get_sqlite_query(MIGRATE_SECOND, is_script=True)

# Заполнение основной таблицы айдишниками через JOIN
get_sqlite_query(MIGRATE_JOIN, is_script=False)

