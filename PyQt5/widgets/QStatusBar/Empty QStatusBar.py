# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 300)

        statusBar = self.statusBar()
        statusBar.setStyleSheet('font-size: 16px; font-weight: bold;')
        statusBar.showMessage('Hello World')
        statusBar.setSizeGripEnabled(False)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
