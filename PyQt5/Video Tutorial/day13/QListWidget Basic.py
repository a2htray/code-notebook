# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem


class Demo(QListWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 200)
        num1 = 1
        num2 = 2
        num3 = 3
        num4 = 4
        num5 = 5
        num6 = 6
        num7 = 7

        self.addItem(str(num1))
        self.addItem(str(num3))
        self.addItem(QListWidgetItem(str(num5)))
        self.addItems((str(num6), str(num7)))

        self.insertItem(1, str(num2))
        self.insertItem(3, str(num4))

        self.itemDoubleClicked.connect(self.displayItem)

        # self.clicked.connect(self.displayItem)

    def displayItem(self, item):
        print(self.currentItem().text())
        print(item.text())
        print(self.currentIndex().row())
        print(self.currentRow())


if __name__ == '__main__':
    app = QApplication([])

    demo = Demo()
    demo.show()

    sys.exit(app.exec())
