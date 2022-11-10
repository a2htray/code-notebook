# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QHeaderView, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItem, QStandardItemModel


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 400)
        layout = QVBoxLayout()

        leSearch = QLineEdit()
        leSearch.setStyleSheet('font-size: 25px; border: 1px dashed #CCCCCC;')

        table = QTableView()
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        fruits = ('Apple', 'Banana', 'Orange')
        model = QStandardItemModel(len(fruits), 1)
        for row, fruit in enumerate(fruits):
            model.setItem(row, 0, QStandardItem(fruit))
        proxyModel = QSortFilterProxyModel()
        proxyModel.setSourceModel(model)
        proxyModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        proxyModel.setFilterKeyColumn(0)

        table.setModel(proxyModel)

        leSearch.textChanged.connect(proxyModel.setFilterRegExp)

        layout.addWidget(leSearch)
        layout.addWidget(table)

        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication([])

    demo = Demo()
    demo.show()

    sys.exit(app.exec())
