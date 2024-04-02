import sys
from PyQt5 import QtWidgets, uic, QtGui

ui_file = "binary_tree.ui"
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return Node, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False
    def append(self, obj):

        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        return obj

    def show_tree(self, node, level=0, prefix=""):
        if node is not None:
            self.show_tree(node.right, level + 1, "R:")
            print(" " * 4 * level + prefix + str(node.data))
            self.show_tree(node.left, level + 1, "L:")


    def __del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.right = s.left

        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left



    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)

        return node, parent


    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None
        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)





class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(ui_file, self)
        self.pushButton.clicked.connect(self.get_numbers)

    def get_numbers(self):
        numbers = self.lineEdit.text().split()

        all_ok = True
        for i in numbers:
            if not i.strip().isdigit():
                all_ok = False
                break


        if all_ok:
            tree = Tree()
            for x in numbers:
                self.tree.append(Node(x))
            result_text = self.tree.show_tree()
            self.label_8.setText(result_text)


        else:
            if not all_ok:
                error_message = "В Вашей записи обнаружены символы вместо чисел. Пожалуйста, исправьте!"
                self.error_dialog = ErrorDialog(error_message)
                self.error_dialog.exec_()





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
