import sys

from PyQt5 import uic
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from Grabber import (GLWidget)
from Sphere_test import (Sphere)

class GUIModel(object):
    @classmethod
    def create(cls, parent):
        form_class, base_class = loadUiType('space_gui.ui')

        ui = form_class()
        ui.setupUi(parent)

        return ui

class App(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        ui = GUIModel.create(self)

        widget = Sphere()
        ui.gridLayout.addWidget(widget, 0, 0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())