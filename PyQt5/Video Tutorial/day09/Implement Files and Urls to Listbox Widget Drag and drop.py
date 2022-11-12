# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QListWidget, QApplication, QWidget, QPushButton, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDragEnterEvent, QDragMoveEvent, QDropEvent


class ListboxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(600, 600)

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event: QDragMoveEvent) -> None:
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent) -> None:
        if event.mimeData().hasUrls():
            event.accept()
            items = []
            for url in event.mimeData().urls():
                if url.isLocalFile():
                    items.append(url.toLocalFile())
                else:
                    items.append(url.toString())
            self.addItems(items)
        else:
            event.ignore()


class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200, 600)
        self.listView = ListboxWidget(self)

        self.button = QPushButton('Get Value', self)
        self.button.setGeometry(800, 50, 100, 50)

        self.button.clicked.connect(self.getSelectedItem)

    def getSelectedItem(self):
        index = self.listView.currentIndex()
        item = self.listView.currentItem()

        if index and item:
            msg = QMessageBox(self)
            msg.setText(f'index: {index}, item: {item.text()}')
            msg.exec()



if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())
