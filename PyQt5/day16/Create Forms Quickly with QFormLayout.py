# -*- coding=utf-8 -*-
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QFormLayout,
    QPushButton,
    QLabel,
    QLineEdit,
)
from PyQt5.Qt import (
    Qt,
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QHBoxLayout Example')

        layout = QFormLayout()

        layout.addRow(QLabel('Name'), QLineEdit('enter your name'))
        layout.addRow(QLabel('Something else'), QLineEdit('xxx'))

        self.setLayout(layout)

        print(self.children())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
