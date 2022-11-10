# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence


class HyperLinkLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet('font-size: 35px;')
        self.setOpenExternalLinks(True)
        self.setParent(parent)


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        linkTemplate = '<a href={0}>{1}</a>'
        label1 = HyperLinkLabel(self)
        label1.setText(linkTemplate.format('https://google.com', 'Google.com'))

        label2 = HyperLinkLabel(self)
        label2.setText(linkTemplate.format('https://microsoft.com', 'Microsoft.com'))

        layout.addWidget(label1)
        layout.addWidget(label2)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])

    demo = Demo()
    demo.show()

    sys.exit(app.exec())

