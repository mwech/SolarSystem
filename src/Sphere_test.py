__author__ = 'arif'

import time


from PyQt5.QtWidgets import (QApplication, QMessageBox, QSplashScreen)
from PyQt5.QtGui import (QPixmap)

try:
    from OpenGL.GLUT import *

except ImportError:
    app = QApplication(sys.argv)
    QMessageBox.critical(None, "OpenGL grabber", "PyOpenGL must be installed to run this example.", QMessageBox.Ok)
    sys.exit(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    glutInit(sys.argv)

    splash_pix = QPixmap('Splashscreen_v2.jpg')
    splash = QSplashScreen(splash_pix)
    splash.setMask(splash_pix.mask())
    splash.show()

    time.sleep(3)

    splash.hide()

    sys.exit(app.exec_())