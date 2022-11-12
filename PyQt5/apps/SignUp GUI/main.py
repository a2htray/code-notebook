# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt


class SignUpWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initializeUI()

        self.show()

    def initializeUI(self):
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()

        self.lbNewUserTitle = QLabel('Create New User', self)
        self.lbNewUserTitle.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.lbNewUserTitle.setStyleSheet('font-size: 22px; padding: 10px; font-weight: bold;')
        layout.addWidget(self.lbNewUserTitle)

        self.lbNewUserPicture = QLabel(self)
        self.lbNewUserPicture.setPixmap(QPixmap('./assets/new_user_icon.png'))
        self.lbNewUserPicture.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.lbNewUserPicture)

        self.displayLineEditors(layout)

        self.btnSignUp = QPushButton('Sign Up', self)
        self.btnSignUp.clicked.connect(self.handleSignUpClicked)
        layout.addWidget(self.btnSignUp, Qt.AlignCenter)
        layout.addStretch(Qt.StretchTile)

        self.setLayout(layout)

    def handleSignUpClicked(self):
        username = self.ledtUsername.text().strip()
        fullname = self.ledtFullname.text().strip()
        password = self.ledtPassword.text().strip()
        passwordConfirm = self.ledtPasswordConfirm.text().strip()

        if not username:
            QMessageBox.warning(self, 'Warning', 'Username is empty!', QMessageBox.Yes, QMessageBox.Yes)
            return

        if not fullname:
            QMessageBox.warning(self, 'Warning', 'Fullname is empty!', QMessageBox.Yes, QMessageBox.Yes)
            return

        if not password:
            QMessageBox.warning(self, 'Warning', 'Password is empty!', QMessageBox.Yes, QMessageBox.Yes)
            return

        if not passwordConfirm:
            QMessageBox.warning(self, 'Warning', 'Confirmed password is empty!', QMessageBox.Yes, QMessageBox.Yes)
            return

        if password != passwordConfirm:
            QMessageBox.warning(self, 'Warning', 'The passwords you enter are not match, please try again.',
                                QMessageBox.Yes, QMessageBox.Yes)
            return

        QMessageBox.information(self, 'Information', 'Register successfully!', QMessageBox.Yes, QMessageBox.Yes)

        self.clearUserEnterContent()

    def clearUserEnterContent(self):
        self.ledtUsername.setText('')
        self.ledtFullname.setText('')
        self.ledtPassword.setText('')
        self.ledtPasswordConfirm.setText('')
        self.ledtUsername.setFocus()

    def displayLineEditors(self, mainLayout: QVBoxLayout):
        widget = QWidget(self)
        layout = QGridLayout(self)

        layout.addWidget(QLabel('Username'), 0, 0)
        self.ledtUsername = QLineEdit(self)
        layout.addWidget(self.ledtUsername, 0, 1)

        layout.addWidget(QLabel('Fullname'), 1, 0)
        self.ledtFullname = QLineEdit(self)
        layout.addWidget(self.ledtFullname, 1, 1)

        layout.addWidget(QLabel('Password'), 2, 0)
        self.ledtPassword = QLineEdit(self)
        self.ledtPassword.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.ledtPassword, 2, 1)

        layout.addWidget(QLabel('Confirm'), 3, 0)
        self.ledtPasswordConfirm = QLineEdit(self)
        self.ledtPasswordConfirm.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.ledtPasswordConfirm, 3, 1)

        widget.setLayout(layout)
        mainLayout.addWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignUpWindow()
    sys.exit(app.exec())
