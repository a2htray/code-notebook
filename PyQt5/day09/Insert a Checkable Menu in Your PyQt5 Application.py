# -*- coding=utf-8 -*-
r"""
"""

import sys
import calendar
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu = self.menuBar().addMenu('Months')
        self.menu.triggered.connect(self.printMonth)
        for i in range(1, 13):
            action = self.menu.addAction(calendar.month_name[i])
            action.setCheckable(True)

    def printMonth(self, action: QAction):
        print(action.text(), action.isChecked())


if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())
