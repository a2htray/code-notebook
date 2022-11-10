# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QCalendarWidget, QApplication
from PyQt5.QtCore import QDate
import win32com.client as win32

excelApp = win32.Dispatch('Excel.Application')
excelApp.visible = True


class CalendarWidget(QCalendarWidget):
    def __init__(self):
        super().__init__()
        self.clicked.connect(self.pickDate)

    def pickDate(self, date: QDate):
        try:
            excelApp.Selection.value = date.toPyDate().strftime('%Y-%m-%d')
        except Exception as e:
            print(e)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    demo = CalendarWidget()
    demo.show()
    sys.exit(app.exec_())
