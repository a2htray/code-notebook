# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QLineEdit


class DemoApp(QWidget):
    def __init__(self):
        super().__init__()
        companyList = ['Google', 'Facebook', 'Apple']

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(50, 50, 300, 30)

        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(50, 100, 300, 30)
        self.comboBox.addItems(companyList)

        self.btn = QPushButton('Click', self)
        self.btn.setGeometry(50, 150, 300, 30)
        self.btn.clicked.connect(self.addComboxItem)

    def addComboxItem(self):
        text = self.lineEdit.text()
        self.comboBox.addItem(text)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    demo = DemoApp()
    demo.show()
    sys.exit(app.exec_())
