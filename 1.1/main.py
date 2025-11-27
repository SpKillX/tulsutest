import sys
import os
from PyQt5 import QtWidgets, uic

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.hello_button.clicked.connect(self.show_message)

    def show_message(self):
        QtWidgets.QMessageBox.information(self, "Привет", "Привет")


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())