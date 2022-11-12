# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFormLayout, QVBoxLayout, QComboBox, QSpinBox, QHBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont


class Order(QWidget):
    def __init__(self, size: QSize):
        super().__init__()
        self._size = size
        self._font = QFont('Open sans', 24)

        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle('Order GUI')
        self.resize(self._size)
        layout = QVBoxLayout()
        self.lbTitle = QLabel('Select 2 items you had for lunch and their price.')
        self.lbTitle.setFont(QFont('Open Sans', 24))
        layout.addWidget(self.lbTitle, alignment=Qt.AlignCenter)

        hbl0 = QHBoxLayout()
        self.cbbItem = QComboBox()
        for item in ['Price', 'Meat', 'Drink']:
            self.cbbItem.addItem(item)
        hbl0.addWidget(self.cbbItem)
        self.sbPrice = QSpinBox()
        self.sbPrice.setRange(10, 35)
        self.sbPrice.setPrefix('$')
        hbl0.addWidget(self.sbPrice)

        layout.addLayout(hbl0)
        self.setLayout(layout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Order(QSize(600, 400))
    sys.exit(app.exec())
