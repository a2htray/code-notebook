# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QFileSystemModel, QVBoxLayout
from PyQt5.QtCore import QModelIndex


class AppDemo(QWidget):
    def __init__(self, dirPath):
        super().__init__()
        appWidth = 800
        appHeight = 300

        self.setWindowTitle('File System Viewer')
        self.setGeometry(300, 300, appWidth, appHeight)

        self.model = QFileSystemModel()
        self.model.setRootPath(dirPath)

        self.treeView = QTreeView()
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(dirPath))
        self.treeView.setColumnWidth(0, 250)
        self.treeView.setAlternatingRowColors(True)

        layout = QVBoxLayout()
        layout.addWidget(self.treeView)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = AppDemo(r'C:\Users')
    demo.show()

    sys.exit(app.exec_())