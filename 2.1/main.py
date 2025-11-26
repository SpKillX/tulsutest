import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)

        self.save_button.clicked.connect(self.save_note)
        self.listWidget.itemClicked.connect(self.load_note)

        self.notes_dir = "notes"
        if not os.path.exists(self.notes_dir):
            os.makedirs(self.notes_dir)

        self.update_notes_list()

    def save_note(self):
        text = self.note_field.toPlainText().strip()

        if not text:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Заметка не может быть пустой!")
            return

        note_name = text[:20].replace('\n', ' ').replace('/', '_').replace('\\', '_')

        filename = f"{note_name}.txt"
        filepath = os.path.join(self.notes_dir, filename)

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(text)

            self.update_notes_list()
            QtWidgets.QMessageBox.information(self, "Успех", f"Заметка сохранена как: {filename}")

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить заметку: {str(e)}")

    def load_note(self, item):
        filename = item.text()
        filepath = os.path.join(self.notes_dir, filename)

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            self.note_field.setPlainText(text)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить заметку: {str(e)}")

    def update_notes_list(self):
        self.listWidget.clear()

        try:
            files = [f for f in os.listdir(self.notes_dir) if f.endswith('.txt')]
            files.sort()

            for file in files:
                self.listWidget.addItem(file)

        except Exception as e:
            print(f"Ошибка при обновлении списка: {e}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())