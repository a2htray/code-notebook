# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QShortcut
from PyQt5.QtGui import QKeySequence


class Demo(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel('Press Ctrl + O')
        self.shortcutPrintMessage = QShortcut(QKeySequence('Ctrl+O'), self)
        self.shortcutPrintMessage.activated.connect(self.printMessage)
        self.shortcutCloseApp = QShortcut(QKeySequence('Ctrl+Q'), self)
        self.shortcutCloseApp.activated.connect(self.closeApp)

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def printMessage(self):
        print('Ctrl + O has been fired.')

    def closeApp(self):
        print(locals(), globals())
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())
