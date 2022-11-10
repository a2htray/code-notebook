# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.Qt import Qt, QTimer

if __name__ == '__main__':
    app = QApplication(sys.argv)

    label = QLabel('<font color=Green size=12>Hello World</font>')
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    label.show()

    QTimer.singleShot(2000, app.quit)
    sys.exit(app.exec())
