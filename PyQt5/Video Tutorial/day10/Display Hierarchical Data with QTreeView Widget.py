# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTreeView
from PyQt5.Qt import QStandardItem, QStandardItemModel, QModelIndex
from PyQt5.QtGui import QFont, QColor


class StandardItem(QStandardItem):
    def __init__(self, txt='', fontSize=12, setBold=False, color=QColor(0, 0, 0)):
        super().__init__()
        font = QFont('Open sans', fontSize)
        font.setBold(setBold)
        self.setEditable(False)
        self.setForeground(color)
        self.setText(txt)
        self.setFont(font)


class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('World Diagram')
        self.resize(500, 700)

        treeView = QTreeView(self)
        treeView.setHeaderHidden(True)
        treeView.collapsed.connect(self.treeViewCollapsed)

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()

        self.hierarchicalData = [
            ['America', ['California', ['San Francisco', 'San Jose', 'Oakland']], ['Texas', ['Austin', 'Dallas', 'Houston']]],
            ['Canada', ['Alberta'], ['British Columbia'], ['Ontario']],
        ]

        for countryData in self.hierarchicalData:
            countryItem = self.createStandardItem(countryData[0])
            for stateData in countryData[1:]:
                stateItem = self.createStandardItem(stateData[0])
                for cityData in stateData[1:]:
                    cityItem = self.createStandardItem(cityData[0])
                    stateItem.appendRow(cityItem)
                countryItem.appendRow(stateItem)
            rootNode.appendRow(countryItem)

        treeView.setModel(treeModel)

        self.setCentralWidget(treeView)

    def createStandardItem(self, txt):
        return StandardItem(txt)

    def treeViewCollapsed(self, index: QModelIndex):
        print(index.data(), index.row())

if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())