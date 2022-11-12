# -*- coding=utf-8 -*-
r"""
"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QRect, QPropertyAnimation


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.baseHeight = 50
        self.extendHeight = 400

        self.setGeometry(QRect(200, 200, 200, self.baseHeight))

        self.button = QPushButton('Expand', self)
        self.button.move(10, 10)
        self.button.clicked.connect(self.resizeWindow)

        self.animation = QPropertyAnimation(self, b'geometry')

    def resizeWindow(self):
        currentHeight = self.height()
        print(f'current height: {currentHeight}')

        if currentHeight == self.baseHeight:
            height = self.extendHeight
            self.button.setText('Expand')
        else:
            height = self.baseHeight
            self.button.setText('Shrink')

        self.animation.setDuration(400)
        self.animation.setStartValue(QRect(200, 200, 200, currentHeight))
        self.animation.setEndValue(QRect(200, 200, 200, height))
        self.animation.start()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec_())
