import sqlite3


def create_database_and_table():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS test (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_text TEXT NOT NULL,
            test_num INTEGER NOT NULL
        )
    ''')

    test_data = [
        ('test1', 20),
        ('dfsggdf', 1),
        ('1234', 19),
        ('test2', 220),
        ('test3', 15)
    ]

    cursor.executemany('INSERT INTO test (test_text, test_num) VALUES (?, ?)', test_data)

    conn.commit()
    conn.close()

create_database_and_table()