# -*- coding=utf-8 -*-
r"""
"""
import sys
import requests
from PyQt5.QtWidgets import QMainWindow, QApplication, QTreeView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QFont, QColor, QImage

webImages = [
    {'name': 'Baidu', 'url': 'https://www.baidu.com/img/flexible/logo/pc/result.png'},
    {'name': 'Tencent', 'url': 'https://www.tencent.com/img/index/tencent_logo.png'},
]


def mapImageData(webImage):
    webImage['binData'] = requests.get(webImage['url']).content
    return webImage


webImages = list(map(mapImageData, webImages))


class StandardItem(QStandardItem):
    def __init__(self, txt='', imageBinData=b'', fontSize=12, setBold=False, color=QColor(0, 0, 0)):
        super().__init__()
        font = QFont('Open Sans', fontSize)
        font.setBold(setBold)
        self.setFont(font)
        self.setEditable(False)
        self.setForeground(color)
        self.setText(txt)

        if imageBinData:
            image = QImage()
            image.loadFromData(imageBinData)
            self.setData(image, Qt.DecorationRole)


class Demo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 400)
        treeView = QTreeView()
        treeView.setHeaderHidden(True)
        treeView.header().setStretchLastSection(True)
        treeView.setMinimumSize(-1, 50)

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()

        for webImage in webImages:
            item = StandardItem(txt=webImage['name'], imageBinData=webImage['binData'], fontSize=12, setBold=True)
            rootNode.appendRow(item)

        treeView.setModel(treeModel)
        treeView.expandAll()

        self.setCentralWidget(treeView)


if __name__ == '__main__':
    app = QApplication([])

    demo = Demo()
    demo.show()

    sys.exit(app.exec())