# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMdiArea, QTextEdit, QPushButton, QCalendarWidget
from PyQt5.Qt import Qt


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        workspace = QMdiArea(self)
        workspace.resize(self.rect().width(), self.rect().height())

        self.calendar = QCalendarWidget()
        # self.calendar.clicked.connect(lambda _: print(self.calendar.date))
        workspace.addSubWindow(self.calendar, Qt.Window)
        self.button = QPushButton('My Button')
        workspace.addSubWindow(self.button)
        self.editor = QTextEdit()
        workspace.addSubWindow(self.editor)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec_())
