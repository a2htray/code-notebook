# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QStyledItemDelegate, QWidget, QStyleOptionViewItem, QTableWidgetItem
from PyQt5.QtCore import QModelIndex


class ReadOnlyDelegate(QStyledItemDelegate):
    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex):
        print(parent, option, index)
        return


class AppDemo(QTableWidget):
    def __init__(self):
        super().__init__(5, 5)
        self.resize(650, 650)
        for i in range(5):
            for j in range(5):
                item = QTableWidgetItem(f'{i}, {j}')
                self.setItem(i, j, item)

        delegate = ReadOnlyDelegate()
        # self.setItemDelegate(delegate)
        self.setItemDelegateForRow(0, delegate)  # 第 1 行只读
        self.setItemDelegateForColumn(0, delegate)  # 第 2 列只读


if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())
