__author__ = 'arif'

import sys, time

from PyQt5 import uic
from PyQt5.uic import loadUiType
from PyQt5.QtGui import (QPixmap)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox, QSplashScreen)
from Grabber import (GLWidget)
from Sphere import (Sphere)

try:
    from OpenGL.GLUT import *

except ImportError:
    app = QApplication(sys.argv)
    QMessageBox.critical(None, "OpenGL grabber", "PyOpenGL must be installed to run this example.", QMessageBox.Ok)
    sys.exit(1)


class App(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        form_class, base_class = loadUiType('space_gui.ui')
        ui = form_class()
        ui.setupUi(self)

        widget = GLWidget()
        ui.gridLayout.addWidget(widget, 0, 0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    glutInit(sys.argv)

    #Setting the Splashscreen
    splash_pix = QPixmap('texturen/Splashscreen_v1.jpg')
    splash = QSplashScreen(splash_pix)
    splash.setMask(splash_pix.mask())
    splash.show()

    #setting the timer for the splash screen
    time.sleep(3)
    splash.hide()

    window = App()
    window.show()
    sys.exit(app.exec_())