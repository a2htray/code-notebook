# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QAbstractItemView, QBoxLayout


class DemoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.data = [
            [1, 2, 3, 4, 5, 1, 2, 3],
            [1, 2, 3, 4, 5, 1, 2, 3],
            [1, 2, 3, 4, 5, 1, 2, 3],
            [1, 2, 3, 4, 5, 1, 2, 3],
            [1, 2, 3, 4, 5, 1, 2, 3],
            [1, 2, 3, 4, 5, 1, 2, 3],
            [1, 2, 3, 4, 5, 1, 2, 3],
            [1, 2, 3, 4, 5, 1, 2, 3],
        ]
        self.preSelectIdxs = [0, 1, 2]

        self.resize(600, 400)
        self.table = QTableWidget()
        self.table.resize(self.rect().width(), self.rect().height())
        self.table.setRowCount(len(self.data))
        self.table.setColumnCount(len(self.data[0]))
        # 设置 Column 名
        self.table.setHorizontalHeaderLabels([f'Col{i+1}' for i in range(len(self.data[0]))])

        self.table.setSelectionMode(QAbstractItemView.MultiSelection)

        for rowIdx, row in enumerate(self.data):
            for colIdx, item in enumerate(row):
                tableItem = QTableWidgetItem()
                tableItem.setText(str(item))
                self.table.setItem(rowIdx, colIdx, tableItem)

        layout = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addWidget(self.table)
        self.setLayout(layout)

        for rowIdx in self.preSelectIdxs:
            self.table.selectRow(rowIdx)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    demo = DemoApp()
    demo.show()
    sys.exit(app.exec_())
