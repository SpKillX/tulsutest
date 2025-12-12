from flask import Flask, render_template, request, redirect, url_for
from database import init_db, get_db_connection

app = Flask(__name__)

init_db()

@app.route("/")
def index():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        conn = get_db_connection()
        conn.execute('INSERT INTO tasks (title, description) VALUES (?, ?)',
                     (title, description))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        conn.execute('UPDATE tasks SET title = ?, description = ? WHERE id = ?',
                     (title, description, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('edit.html', task=task)

@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

app.run()