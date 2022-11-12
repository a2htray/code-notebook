# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem
from PyQt5.QtGui import QColor


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.list = QListWidget(self)

        colors = [
            'yellow',
            'green',
            'red',
        ]

        for color in colors:
            item = QListWidgetItem(color)
            item.setForeground(QColor(color))
            self.list.addItem(item)


if __name__ == '__main__':
    app = QApplication([])

    demo = Demo()
    demo.show()

    sys.exit(app.exec())
