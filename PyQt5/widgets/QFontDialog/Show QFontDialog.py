# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFontDialog, QPushButton
from PyQt5.QtGui import QFont


class ShowFontDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 200, 200)
        self.btn = QPushButton('字体', self)
        self.btn.clicked.connect(lambda _: print(QFontDialog.getFont(QFont('Helvetica', 10), self)))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShowFontDialog()
    sys.exit(app.exec())