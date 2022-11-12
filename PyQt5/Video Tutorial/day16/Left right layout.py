# -*- coding=utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel)


class TreeMenu(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Tree Menu'))
        self.setLayout(layout)

        self.setStyleSheet('border: 2px dashed #FFCCCC;')


class Workspace(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Workspace'))
        self.setLayout(layout)

        self.setStyleSheet('border: 2px solid #DDFF88;')


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        layout.addWidget(TreeMenu(), 0)
        layout.addWidget(Workspace(), 1)
        self.setLayout(layout)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1260, 600)
        self.setWindowTitle('Left Right Example')

        widget = MainWidget()
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
