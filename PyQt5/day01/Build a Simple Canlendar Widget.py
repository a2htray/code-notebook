# -*- coding=utf-8 -*-
r"""
"""
import calendar
import sys
from datetime import datetime
from PyQt5.QtWidgets import QCalendarWidget, QApplication, QWidget
from PyQt5.QtCore import QDate


class CalendarWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calendar Demo')
        self.setGeometry(100, 100, 450, 400)
        self.initUI()

    def initUI(self):
        self.calendar = QCalendarWidget(self)
        self.calendar.move(20, 20)
        self.calendar.setGridVisible(False)
        self.setDateRange()
        # self.calendar.setSelectedDate()

        self.bindEvents()

    def setDateRange(self):
        currentYear = datetime.now().year
        currentMonth = datetime.now().month

        self.calendar.setMinimumDate(QDate(currentYear, currentMonth - 1, 1))
        self.calendar.setMaximumDate(QDate(currentYear, currentMonth + 1, calendar.monthrange(currentYear, currentMonth + 1)[1]))

    def bindEvents(self):
        """
        @link: https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QCalendarWidget.html#signals
        :return:
        """
        self.calendar.clicked.connect(self._calendarClickEvent)

    def _calendarClickEvent(self, date: QDate):
        print(date)

def main():
    app = QApplication(sys.argv)

    widget = CalendarWidget()
    widget.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
