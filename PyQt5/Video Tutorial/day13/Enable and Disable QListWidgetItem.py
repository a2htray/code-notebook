# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt


class Demo(QListWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 400)
        items = ['Item {0}'.format(item) for item in range(4)]
        disabledFlags = [True, True, False, False]

        for item, disabledFlag in zip(items, disabledFlags):
            lstItem = QListWidgetItem(item)
            if disabledFlag:
                lstItem.setFlags(Qt.NoItemFlags)
            self.addItem(lstItem)

        self.itemPressed.connect(self.displayItem)

    def displayItem(self, item):
        print(item.text())

if __name__ == '__main__':
    app = QApplication([])

    demo = Demo()
    demo.show()

    sys.exit(app.exec())
