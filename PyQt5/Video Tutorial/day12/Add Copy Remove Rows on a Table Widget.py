# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHeaderView, QAbstractItemView, QPushButton, QTableWidget, \
    QTableWidgetItem, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt


class TableWidget(QTableWidget):
    def __init__(self):
        super().__init__(3, 5)
        self.setHorizontalHeaderLabels(list('ABCDE'))
        self.verticalHeader().setDefaultSectionSize(30)
        self.horizontalHeader().setDefaultSectionSize(250)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.setGridStyle(Qt.PenStyle.DashLine)
        self.setShowGrid(True)

    def newRow(self):
        rowCount = self.rowCount()
        self.insertRow(rowCount)

    def removeRow(self):
        currentRow = self.currentRow()
        super().removeRow(currentRow)

    def copyRow(self):
        currentRowIndex = self.currentRow()
        print(currentRowIndex)
        self.insertRow(currentRowIndex+1)
        print('self.insertRow(currentRowIndex+1)')

        for j in range(self.columnCount()):
            if self.item(currentRowIndex, j) is not None:
                self.setItem(currentRowIndex+1, j, QTableWidgetItem(self.item(currentRowIndex, j).text()))


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1600, 600)
        layout = QHBoxLayout()
        table = TableWidget()
        layout.addWidget(table)

        buttonLayout = QVBoxLayout()
        buttonNew = QPushButton('New')
        buttonNew.clicked.connect(table.newRow)
        buttonCopy = QPushButton('Copy')
        buttonCopy.clicked.connect(table.copyRow)
        buttonRemove = QPushButton('Remove')
        buttonRemove.clicked.connect(table.removeRow)

        buttonLayout.addWidget(buttonNew)
        buttonLayout.addWidget(buttonCopy)
        buttonLayout.addWidget(buttonRemove, alignment=Qt.AlignTop)
        layout.addLayout(buttonLayout)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())
