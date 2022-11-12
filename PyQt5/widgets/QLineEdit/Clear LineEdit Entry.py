# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt


class EntryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('QLineEdit Widget')
        self.displayWidgets()

        self.show()

    def displayWidgets(self):
        QLabel('Please enter your name below.', self).move(100, 10)
        nameLabel = QLabel('Name:', self)
        nameLabel.move(70, 50)

        self.nameEntry = QLineEdit(self)
        self.nameEntry.setAlignment(Qt.AlignLeft)
        self.nameEntry.move(130, 50)
        self.nameEntry.resize(200, 20)

        self.clearButton = QPushButton('Clear', self)
        self.clearButton.clicked.connect(self.clearEntries)
        self.clearButton.move(160, 110)

    def clearEntries(self):
        sender = self.sender()
        if sender.text() == 'Clear':
            self.nameEntry.clear()
            self.nameEntry.setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EntryWindow()
    sys.exit(app.exec())
