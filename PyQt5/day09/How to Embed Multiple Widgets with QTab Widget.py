# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QVBoxLayout, QTabWidget, QPushButton, \
    QCalendarWidget


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        mainLayout = QGridLayout(self)
        tab1 = QTabWidget()
        tab2 = QTabWidget()
        mainLayout.addWidget(tab1, 0, 0)
        mainLayout.addWidget(tab2, 0, 1)

        tab1One = QWidget()
        tab1OneLayout = QVBoxLayout()
        tab1OneLayout.addWidget(QLabel('This is a test'))
        tab1OneLayout.addWidget(QPushButton('Test Button'))
        tab1One.setLayout(tab1OneLayout)
        tab1Two = QWidget()
        tab1TwoLayout = QVBoxLayout()
        tab1TwoLayout.addWidget(QLabel('This is also a test'))
        tab1Two.setLayout(tab1TwoLayout)

        tab1.addTab(tab1One, 'Tab 1.1')
        tab1.addTab(tab1Two, 'Tab 1.2')

        tab2One = QTabWidget()
        tab2OneLayout = QVBoxLayout()
        tab2OneLayout.addWidget(QCalendarWidget())
        tab2One.setLayout(tab2OneLayout)

        tab2.addTab(tab2One, 'Tab 2.1')


if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())
