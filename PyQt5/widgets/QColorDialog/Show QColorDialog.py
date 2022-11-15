# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog, QPushButton
from PyQt5.QtGui import QFont


class ShowFontDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 200, 200)
        self.btn = QPushButton('颜色', self)
        self.btn.clicked.connect(lambda _: print(QColorDialog.getColor()))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShowFontDialog()
    sys.exit(app.exec())
