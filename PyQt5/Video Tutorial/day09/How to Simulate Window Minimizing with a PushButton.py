# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 600)
        self.button = QPushButton('Hide Window', self)
        self.button.clicked.connect(self.hideWindow)

    def hideWindow(self):
        self.showMinimized()


if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())
