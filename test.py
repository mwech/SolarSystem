import sys

from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import (QApplication, QMainWindow)


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        form_class, base_class = loadUiType('space_gui.ui')
        self.ui = form_class()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())