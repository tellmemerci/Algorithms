import sys
from PyQt5 import QtWidgets, uic

# Путь к вашему файлу .ui
ui_file = "calculator.ui"

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(ui_file, self)
        self.label.clear()
        self.pushButton_18.setText("Х")
        self.pushButton_22.setText("^")
        self.pushButton.clicked.connect(lambda: self.add_number('1'))
        self.pushButton_2.clicked.connect(lambda: self.add_number('2'))
        self.pushButton_3.clicked.connect(lambda: self.add_number('3'))
        self.pushButton_4.clicked.connect(lambda: self.add_number('4'))
        self.pushButton_5.clicked.connect(lambda: self.add_number('5'))
        self.pushButton_6.clicked.connect(lambda: self.add_number('6'))
        self.pushButton_7.clicked.connect(lambda: self.add_number('7'))
        self.pushButton_8.clicked.connect(lambda: self.add_number('8'))
        self.pushButton_9.clicked.connect(lambda: self.add_number('9'))
        self.pushButton_10.clicked.connect(lambda: self.add_number('0'))
        self.pushButton_12.clicked.connect(lambda: self.add_number(' ( '))
        self.pushButton_13.clicked.connect(lambda: self.add_number(' ) '))
        self.pushButton_14.clicked.connect(lambda: self.add_number(' + '))
        self.pushButton_15.clicked.connect(lambda: self.add_number(' - '))
        self.pushButton_16.clicked.connect(lambda: self.add_number(' / '))
        self.pushButton_18.clicked.connect(lambda: self.add_number(' X '))
        self.pushButton_11.clicked.connect(self.result)
        self.pushButton_17.clicked.connect(self.clear)


    def clear(self):
        self.label.clear()


    def add_number(self, number):
        current_text = self.label.text()
        new_text = current_text + number
        self.label.setText(new_text)

    def result(self):
        str = self.label.text()
        str = str.split()
        print(str)






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
