import sqlite3


def delete_record_by_id(record_id):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM test WHERE id = ?', (record_id,))
    record = cursor.fetchone()

    if record:
        cursor.execute('DELETE FROM test WHERE id = ?', (record_id,))
        conn.commit()
        print(f"Запись с ID={record_id} удалена.")
    else:
        print(f"Запись с ID={record_id} не найдена.")

    conn.close()


delete_record_by_id(1)