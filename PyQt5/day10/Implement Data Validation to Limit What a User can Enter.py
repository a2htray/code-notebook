# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPlainTextEdit, QVBoxLayout
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QKeyEvent


class TextEdit(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        regexp = QRegExp(r'^[a-zA-Z]*$')
        self.validator = QRegExpValidator(regexp)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        print('keyPressEvent', event.text(), self.validator.validate(event.text(), 0))
        state = self.validator.validate(event.text(), 0)
        if state[0] == QRegExpValidator.Acceptable or state[1] in ('\x08', '\r'):
            super().keyPressEvent(event)


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)

        layout = QVBoxLayout()
        validator = QRegExpValidator(QRegExp(r'[0-9]+'))

        self.lineEdit = QLineEdit()
        self.lineEdit.setValidator(validator)
        layout.addWidget(self.lineEdit)

        self.textEdit = TextEdit()
        layout.addWidget(self.textEdit)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())
