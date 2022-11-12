# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt


class ItemWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(100, 50)
        layout = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def setText(self, text):
        self.label.setText(text)
        return self


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 400)
        items = ['Item {0}'.format(idx) for idx in range(5)]
        self.listWidget = QListWidget(self)
        self.listWidget.addItems(items)

        self.itemWidget = ItemWidget()

        self.listWidget.itemPressed.connect(self.showItemWidget)

    def showItemWidget(self, item: QListWidgetItem):
        self.itemWidget.setText(item.text()).show()


if __name__ == '__main__':
    app = QApplication([])

    demo = Demo()
    demo.show()

    sys.exit(app.exec())
