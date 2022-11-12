# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp


class SecondaryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 60)
        self.setWindowTitle('xxx')
        self.labelInformation = QLabel(self)

    def setText(self, text):
        self.labelInformation.setText(text)

    def show(self) -> None:
        super().show()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        labelName = QLabel('Name')
        self.lineEditName = QLineEdit()

        labelAge = QLabel('Age')
        self.lineEditAge = QLineEdit()
        validatorAge = QRegExpValidator(QRegExp(r'[1-9]{1}[0-9]*'))
        self.lineEditAge.setValidator(validatorAge)

        pushButtonPass = QPushButton('Pass Data')
        pushButtonPass.clicked.connect(self.handleButtonPassClick)

        layout.addWidget(labelName)
        layout.addWidget(self.lineEditName)
        layout.addWidget(labelAge)
        layout.addWidget(self.lineEditAge)
        layout.addWidget(pushButtonPass)

        self.setLayout(layout)

        self.secondaryWindow = SecondaryWindow()

    def handleButtonPassClick(self):
        self.secondaryWindow.setText(f'Name: {self.lineEditName.text()}, Age: {self.lineEditAge.text()}')
        self.secondaryWindow.show()


if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
