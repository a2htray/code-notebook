# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QLineEdit, QPushButton, QCheckBox
from PyQt5.QtGui import QFont, QCloseEvent
from PyQt5.QtCore import Qt


class LoginUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 230)
        self.setWindowTitle('Login GUI')
        self.loginUserInterface()

        self.show()

    def loginUserInterface(self):
        loginLabel = QLabel(self)
        loginLabel.setText('login')
        loginLabel.move(180, 10)
        loginLabel.setFont(QFont('Arial', 20))

        nameLabel = QLabel('username:', self)
        nameLabel.move(30, 60)

        self.nameEntry = QLineEdit(self)
        self.nameEntry.move(110, 60)
        self.nameEntry.resize(220, 20)

        passwordLabel = QLabel('password:', self)
        passwordLabel.move(30, 90)

        self.passwordEntry = QLineEdit(self)
        self.passwordEntry.move(110, 90)
        self.passwordEntry.resize(220, 20)

        signInButton = QPushButton('login', self)
        signInButton.move(100, 140)
        signInButton.resize(200, 40)
        signInButton.clicked.connect(self.handleLoginClicked)

        showPasswordCheckbox = QCheckBox('show password', self)
        showPasswordCheckbox.move(110, 115)
        showPasswordCheckbox.stateChanged.connect(self.handleShowPassword)
        showPasswordCheckbox.toggle()
        showPasswordCheckbox.setChecked(False)

        notaMemberLabel = QLabel('not a member?', self)
        notaMemberLabel.move(70, 200)

        signUpButton = QPushButton('sign up', self)
        signUpButton.move(160, 195)
        signUpButton.clicked.connect(self.handleCreateNewUser)

    def handleLoginClicked(self):
        username = self.nameEntry.text()
        password = self.passwordEntry.text()

        db = {}

        try:
            with open('./assets/users.txt', 'r') as f:
                for line in f:
                    userPaswordPair = line.split(' ')
                    db[userPaswordPair[0]] = userPaswordPair[1].strip('\n')
        except FileNotFoundError:
            pass

        if username in db and db[username] == password:
            QMessageBox.information(self, 'Information', 'Login Successfully!', QMessageBox.Ok, QMessageBox.Ok)
            self.close()
        else:
            QMessageBox.warning(self, 'Warning', 'The username or password is incorrect', QMessageBox.Close,
                                QMessageBox.Close)

    def handleShowPassword(self, state):
        if state == Qt.Checked:
            self.passwordEntry.setEchoMode(QLineEdit.Normal)
        else:
            self.passwordEntry.setEchoMode(QLineEdit.Password)

    def handleCreateNewUser(self):
        pass

    def closeEvent(self, e: QCloseEvent) -> None:
        quitResponse = QMessageBox.question(self, 'Quit Application', 'Are you sure to quit',
                             QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
        if quitResponse == QMessageBox.No:
            e.ignore()
        else:
            e.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginUI()
    sys.exit(app.exec())
