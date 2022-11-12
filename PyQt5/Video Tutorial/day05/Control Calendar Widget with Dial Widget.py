# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QDial, QBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(700, 500)

        self.dial = QDial()
        self.dial.resize(100, 500)
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.valueChanged.connect(self.updateCalendar)

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setSelectedDate(QDate.currentDate())

        layout = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addWidget(self.calendar)
        layout.addWidget(self.dial)

        self.setLayout(layout)

    def updateCalendar(self, value):
        self.calendar.setSelectedDate(self.calendar.selectedDate().addDays(value))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec_())
