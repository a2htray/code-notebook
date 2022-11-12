# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 80)
        QLabel('Password', self).move(10, 12)

        self.passwordEntry = QLineEdit(self)
        self.passwordEntry.setEchoMode(QLineEdit.Password)
        self.passwordEntry.move(80, 10)

        self.cbShowPassword = QCheckBox('show password', self)
        self.cbShowPassword.move(80, 40)
        self.cbShowPassword.stateChanged.connect(self.handleShowPasswordStateChanged)

        self.show()

    def handleShowPasswordStateChanged(self, state):
        if state == Qt.CheckState.Checked:
            self.passwordEntry.setEchoMode(QLineEdit.Normal)
        else:
            self.passwordEntry.setEchoMode(QLineEdit.Password)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
