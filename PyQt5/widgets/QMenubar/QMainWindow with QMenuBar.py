# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, QMenuBar


class BasicMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 350, 350)
        self.setWindowTitle('Basic Menu Example')
        self.createMenu()
        self.show()

    def createMenu(self):
        actExit = QAction('Exit', self)

        actExit.setShortcut('Ctrl+Q')
        actExit.triggered.connect(self.close)

        menuBar: QMenuBar = self.menuBar()
        # menuBar.setNativeMenuBar(False)
        mnFile = menuBar.addMenu('File')
        mnFile.addAction(actExit)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicMenu()
    sys.exit(app.exec())
