import sys
from PyQt5 import QtWidgets, uic, QtGui
from Class import *
ui_file = "binary_tree.ui"
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(ui_file, self)
        self.pushButton.clicked.connect(self.get_numbers)
    def get_numbers(self):
        numbers = self.lineEdit.text().split()
        numbers_m = []
        for i in range(len(numbers)):
            numbers_m.append(int(numbers[i]))
        print(numbers_m)

        all_ok = True
        for i in numbers:
            if not i.strip().isdigit():
                all_ok = False
                break

        if all_ok:
            t = Tree()
            for i in numbers_m:
                t.append(Node(i))
            result = t.show_wide_tree(t.root)
            self.label_8.setText(result)
            pass
        else:
            if not all_ok:
                error_message = "В Вашей записи обнаружены символы вместо чисел. Пожалуйста, исправьте!"
                self.error_dialog = ErrorDialog(error_message)
                self.error_dialog.exec_()

        return numbers

class ErrorDialog(QDialog):
    def __init__(self, message, parent=None):
        super(ErrorDialog, self).__init__(parent)
        uic.loadUi("error_mes_tree.ui", self)
        self.show()
        self.label_2.setText(message)
        self.pushButton.setText('Ок')
        self.pushButton.clicked.connect(self.close_app)
    def close_app(self):
        self.close()





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
