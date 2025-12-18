import sqlite3
import time


def create_table():
    conn = sqlite3.connect('indexed.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    for i in range(1, 10001):
        cursor.execute('INSERT INTO products (name, category, price) VALUES (?, ?, ?)',
                       (f'Товар {i}', f'Категория {i % 10}', i * 10.5))

    conn.commit()
    conn.close()

def create_index():
    conn = sqlite3.connect('indexed.db')
    cursor = conn.cursor()

    cursor.execute('CREATE INDEX IF NOT EXISTS idx_category ON products(category)')
    conn.commit()
    conn.close()


def search_without_index():
    conn = sqlite3.connect('indexed.db')
    cursor = conn.cursor()

    start_time = time.time()
    cursor.execute('SELECT * FROM products WHERE category = ?', ('Категория 5',))
    rows = cursor.fetchall()
    end_time = time.time()

    print(f"Без индекса: найдено {len(rows)} записей за {end_time - start_time:.4f} сек.")
    conn.close()


def search_with_index():
    conn = sqlite3.connect('indexed.db')
    cursor = conn.cursor()

    start_time = time.time()
    cursor.execute('SELECT * FROM products WHERE category = ?', ('Категория 5',))
    rows = cursor.fetchall()
    end_time = time.time()

    print(f"С индексом: найдено {len(rows)} записей за {end_time - start_time:.4f} сек.")
    conn.close()


create_table()
search_without_index()
create_index()
search_with_index()