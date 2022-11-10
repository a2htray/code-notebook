# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QPushButton,
)
from PyQt5.Qt import (
    Qt,
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()

        layout.addWidget(QPushButton('1x1'), 0, 0)
        layout.addWidget(QPushButton('2x1'), 0, 1, 1, 2)
        layout.addWidget(QPushButton('1x1'), 1, 0)
        layout.addWidget(QPushButton('2x2'), 1, 1, 2, 2, Qt.AlignJustify)
        layout.addWidget(QPushButton('1x1'), 2, 0)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
