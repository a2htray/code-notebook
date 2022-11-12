# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.Qt import Qt
from PyQt5.QtGui import QKeyEvent


class Demo(QWidget):
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        print(event.key(), event.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = Demo()
    demo.show()

    sys.exit(app.exec_())