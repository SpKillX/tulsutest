import sqlite3

def select_data_from_table():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM test')
    rows = cursor.fetchall()

    if rows:
        print("Список:")
        for row in rows:
            print(f"ID: {row[0]}, Текст: {row[1]}, Число: {row[2]}")
    else:
        print("В таблице нет данных.")

    conn.close()

select_data_from_table()