# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import (QApplication, QPushButton)
from PyQt5.QtCore import Qt


class Window(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText('Click')
        self.clicked.connect(self.handleClicked)

    def handleClicked(self):
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.ShiftModifier:
            print('Shift+Click')
        elif modifiers == Qt.ControlModifier:
            print('Ctrl+Click')
        else:
            print('Mouse Click')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
