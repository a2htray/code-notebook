import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QFormLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QFormLayout()
        lbUsername = QLabel('&Username:')
        ledtUsername = QLineEdit()
        lbUsername.setBuddy(ledtUsername)
        lbPassword = QLabel('&Password:')
        ledtPassword = QLineEdit()
        lbPassword.setBuddy(ledtPassword)

        layout.addRow(lbUsername, ledtUsername)
        layout.addRow(lbPassword, ledtPassword)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
