# -*- coding=utf-8 -*-
r"""
"""

import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView, \
    QPushButton, QItemDelegate, QStyleOptionViewItem, QLineEdit
from PyQt5.QtCore import QModelIndex
from PyQt5.QtGui import QDoubleValidator


class FloatItemDelegate(QItemDelegate):
    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex) -> QWidget:
        print('FloatItemDelegate.createEditor')
        print(parent.objectName())
        editor = QLineEdit()
        editor.setValidator(QDoubleValidator())
        return editor


class DataFrameEditor(QTableWidget):
    def __init__(self, df: pd.DataFrame, parent):
        super().__init__(parent=parent)
        self.df = df
        nRows, nColumns = self.df.shape

        # 一定要提前设置表格的行数与列数
        self.setRowCount(nRows)
        self.setColumnCount(nColumns)

        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setHorizontalHeaderLabels([str(column) for column in self.df.columns])

        for i in range(nRows):
            for j in range(nColumns):
                self.setItem(i, j, QTableWidgetItem(str(self.df.iloc[i, j])))

        self.itemChanged.connect(self.handleItemChanged)
        self.setItemDelegate(FloatItemDelegate())

    def handleItemChanged(self, item: QTableWidgetItem):
        print('DataFrameEditor.handleItemChanged')
        row, column = item.row(), item.column()
        self.updateDataFrame(row, column)

    def updateDataFrame(self, row: int, column: int):
        self.df.iloc[row, column] = float(self.item(row, column).text())


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.dataFrameEditor = DataFrameEditor(pd.DataFrame([
            [2.5, 2.5],
            [3.0, 3.0],
            [3.5, 3.5],
            [4.0, 4.0],
        ], columns=['X', 'Y']), self)

        layout = QVBoxLayout()
        layout.addWidget(self.dataFrameEditor)

        buttonPrint = QPushButton('Print DF')
        buttonPrint.clicked.connect(self.handleBtnPrintClicked)
        buttonExport =QPushButton('Export DF')
        buttonExport.clicked.connect(self.handleBtnExportClicked)
        layout.addWidget(buttonPrint)
        layout.addWidget(buttonExport)

        self.setLayout(layout)

    def handleBtnExportClicked(self):
        print('Demo.handleBtnExportClick')
        self.dataFrameEditor.df.to_csv(r'D:\private\code-notebook\df.csv', index=False)

    def handleBtnPrintClicked(self):
        print('Demo.handleBtnPrintClick')
        print(self.dataFrameEditor.df)


if __name__ == '__main__':
    app = QApplication([])

    demo = Demo()
    demo.show()

    sys.exit(app.exec())
