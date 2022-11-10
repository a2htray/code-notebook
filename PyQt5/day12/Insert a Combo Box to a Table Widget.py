# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QComboBox, QVBoxLayout


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1600, 500)

        layout = QVBoxLayout()

        self.table = QTableWidget(2, 5)
        self.table.setHorizontalHeaderLabels(list('ABCDE'))
        self.table.setColumnWidth(4, 400)
        self.table.verticalHeader().setDefaultSectionSize(50)
        self.table.horizontalHeader().setDefaultSectionSize(250)

        comboBox = QComboBox()
        comboBox.addItems(['X1', 'X2', 'X3'])
        # comboBox.currentIndexChanged.connect()
        self.table.setCellWidget(0, 4, comboBox)

        layout.addWidget(self.table)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())
