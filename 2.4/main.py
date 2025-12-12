from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')

        if not file or file.filename == '':
            return 'Файл не выбран!'

        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return f'Файл "{file.filename}" загружен <a href="/upload">Ещё файл</a>'

    return redirect(url_for('home'))

app.run()