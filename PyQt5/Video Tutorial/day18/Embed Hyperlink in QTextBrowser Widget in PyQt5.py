# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextBrowser
from PyQt5.QtGui import QTextCursor


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 200)
        layout = QVBoxLayout()

        self.button = QPushButton('Show Content')
        self.button.clicked.connect(self.generateContent)
        self.browser = QTextBrowser()
        layout.addWidget(self.button)
        layout.addWidget(self.browser)

        self.setLayout(layout)
        self.show()

    def generateContent(self):
        self.browser.moveCursor(QTextCursor.Start)
        self.browser.append('Hello World')
        self.browser.append('<a href="https://www.baidu.com">Baidu</a>')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    sys.exit(app.exec())
