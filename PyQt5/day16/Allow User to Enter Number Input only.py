# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import (QApplication, QLineEdit)
from PyQt5.QtGui import QValidator, QIntValidator


class Window(QLineEdit):
    def __init__(self):
        super().__init__()
        self.resize(400, 50)
        self.setStyleSheet('font-size: 24px;')
        self.editingFinished.connect(self.validating)

    def validating(self):
        print('Window.validating')
        rule = QIntValidator(-100, 100)
        validateResult = rule.validate(self.text(), 0)
        print(validateResult)
        if rule.validate(self.text(), 0)[0] == QValidator.Acceptable:
            self.setFocus()
        else:
            self.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())