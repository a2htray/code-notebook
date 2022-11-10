# -*- coding=utf-8 -*-
r"""
展示 DataFrame
"""

import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex

df = pd.DataFrame({
    'Name': ['Mary', 'Jim', 'John'],
    'Age': [22, 24, 28],
    'Gender': ['M', 'F', 'F'],
})


class PandasModel(QAbstractTableModel):
    """将数据集转换成 PyQt 表模型"""
    def __init__(self, data):
        super().__init__(None)
        self._data: pd.DataFrame = data

    def rowCount(self, parent=None) -> int:
        return self._data.shape[0]

    def columnCount(self, parent=None) -> int:
        return self._data.shape[1]

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, section: int, orientation: Qt.Orientation, role=Qt.DisplayRole):
        print(section, orientation, role)
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[section]
        return None


if __name__ == '__main__':
    app = QApplication(sys.argv)

    model = PandasModel(df)
    view = QTableView()
    view.setModel(model)
    view.resize(800, 600)
    view.show()

    sys.exit(app.exec_())

