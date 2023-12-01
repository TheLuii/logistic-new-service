import sqlite3
import openpyxl

# Создаем соединение с базой данных
conn = sqlite3.connect('telegram.db')

# Создаем курсор
cursor = conn.cursor()

# Создаем таблицу с необходимыми столбцами
create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        telegram_id TEXT,
        username TEXT,
        telegram_frist_name TEXT,
        telegram_second_name TEXT,
        company_name TEXT,
        phone TEXT,
        user_role TEXT
    )
'''

cursor.execute(create_table_query)

create_table_direction = '''
    CREATE TABLE IF NOT EXISTS direction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    users_id TEXT,
    direction_name TEXT,
    direction_description TEXT,
    direction_price TEXT,
    direction_sattus TEXT,
    winner TEXT,
    FOREIGN KEY (users_id) REFERENCES users (id)
    )
'''
cursor.execute(create_table_direction)

create_table_query = '''
    CREATE TABLE IF NOT EXISTS directionList (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        telegram_id TEXT,
        company_name TEXT,
        direction TEXT,
        old_price TEXT, 
        new_price TEXT,
        direction_status TEXT
    )
'''

cursor.execute(create_table_query)


# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()


print("База данных создана успешно.")



