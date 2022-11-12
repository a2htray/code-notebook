# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QRadioButton, QStackedWidget, QVBoxLayout, \
    QHBoxLayout
from PyQt5.QtCore import Qt


class WidgetButtons(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        for i in range(4):
            layout.addWidget(QPushButton(f'Button #{i}'))
        self.setLayout(layout)


class WidgetLineEdits(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        for i in range(4):
            layout.addWidget(QLineEdit(f'Widget Button #{i}'))
        self.setLayout(layout)


class WidgetRadioButtons(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        for i in range(4):
            layout.addWidget(QRadioButton(f'Radio Button #{i}'))
        self.setLayout(layout)


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(WidgetButtons())
        self.stackedWidget.addWidget(WidgetLineEdits())
        self.stackedWidget.addWidget(WidgetRadioButtons())
        layout.addWidget(self.stackedWidget)

        buttonPrevious = QPushButton('Previous')
        buttonPrevious.clicked.connect(self.handleButtonPreviousClk)
        buttonNext = QPushButton('Next')
        buttonNext.clicked.connect(self.handleButtonNextClk)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(buttonPrevious)
        buttonLayout.addWidget(buttonNext)
        layout.addLayout(buttonLayout)

        self.setLayout(layout)

    def handleButtonPreviousClk(self):
        currentIndex = self.stackedWidget.currentIndex()
        print(currentIndex)
        self.stackedWidget.setCurrentIndex((currentIndex + 1) % self.stackedWidget.count())

    def handleButtonNextClk(self):
        currentIndex = self.stackedWidget.currentIndex()
        print(currentIndex)
        self.stackedWidget.setCurrentIndex((currentIndex - 1) % self.stackedWidget.count())


if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())
