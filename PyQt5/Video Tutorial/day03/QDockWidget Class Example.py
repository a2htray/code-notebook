# -*- coding=utf-8 -*-
r"""
"""
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QDockWidget, QListWidget, QListWidgetItem
from PyQt5.Qt import Qt


class DockWidgetDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.textEdit = QTextEdit()

        listWidget = QListWidget()
        for item in ['Google', 'Facebook', 'Microsoft', 'Apple']:
            listWidget.addItem(QListWidgetItem(item))

        # https://doc.qt.io/qt-5/qlistwidget.html
        listWidget.itemDoubleClicked.connect(self.listItemDoubleClickEvent)

        dockWidget = QDockWidget()
        dockWidget.setWidget(listWidget)
        dockWidget.setFloating(False)

        self.addDockWidget(Qt.RightDockWidgetArea, dockWidget)
        self.setCentralWidget(self.textEdit)

    def listItemDoubleClickEvent(self, item: QListWidgetItem):
        self.textEdit.setPlainText(item.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = DockWidgetDemo()
    demo.show()

    sys.exit(app.exec_())
