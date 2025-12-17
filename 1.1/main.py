import sqlite3


def create_database_and_table():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_text TEXT NOT NULL,
            test_num INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


create_database_and_table()