# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMenu, QAction


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton('Click Me', self)
        self.button.setStyleSheet('font-size: 25px;')
        self.button.move(150, 150)
        self.button.resize(200, 30)

        self.menu = QMenu()
        self.button.setMenu(self.menu)

        self.menu.addMenu(QMenu('x', self.menu))
        self.menu.addAction(QAction('action', self.menu))


if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())
