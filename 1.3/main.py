import sys
import os
from PyQt5 import QtWidgets, uic


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.equal.clicked.connect(self.calculate)

    def calculate(self):
        try:
            a = float(self.first_field.text())
            b = float(self.second_field.text())
            operation = self.operations.currentText()

            if operation == "+":
                result = a + b
            elif operation == "-":
                result = a - b
            elif operation == "*":
                result = a * b
            elif operation == "/":
                if b != 0:
                    result = a / b
                else:
                    self.result.setText("Ошибка: деление на 0")
                    return
            else:
                result = a + b

            self.result.setText(f"Результат: {result}")

        except ValueError:
            self.result.setText("Ошибка ввода: введите числа")



app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())