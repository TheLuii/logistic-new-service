import sqlite3

dp_path = '../telegram.db'

def get_user_role(ID):
    conn = sqlite3.connect('telegram.db')
    cursor = conn.cursor()

    select_query = '''
                SELECT user_role
                FROM users
                WHERE telegram_id = ?
            '''
    cursor.execute(select_query, (ID,))
    conn.commit()
    result = cursor.fetchone()
    conn.close()

    return result