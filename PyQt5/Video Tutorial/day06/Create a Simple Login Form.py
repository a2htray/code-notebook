# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QGridLayout


class DemoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Form')

        self.labelName = QLabel('Username')
        self.lineEditName = QLineEdit()
        self.lineEditName.setPlaceholderText('enter your username')
        self.labelPassword = QLabel('Password')
        self.lineEditPassword = QLineEdit()
        self.lineEditPassword.setPlaceholderText('enter your password')
        self.pushButton = QPushButton('Login')
        self.pushButton.clicked.connect(self.checkCredential)

        layout = QGridLayout()
        layout.addWidget(self.labelName, 0, 0)
        layout.addWidget(self.lineEditName, 0, 1)
        layout.addWidget(self.labelPassword, 1, 0)
        layout.addWidget(self.lineEditPassword, 1, 1)
        layout.addWidget(self.pushButton, 2, 0, 1, 2)

        self.setLayout(layout)

    def checkCredential(self):
        messageBox = QMessageBox()
        messageBox.setWindowTitle('message')
        messageBox.resize(100, 60)
        if self.lineEditName.text() == 'testuser' and self.lineEditPassword.text() == 'testpassword':
            messageBox.setText('Success')
            messageBox.exec_()
            app.quit()
        else:
            messageBox.setText('Failed')
            messageBox.exec_()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    demo = DemoApp()
    demo.show()
    sys.exit(app.exec_())
