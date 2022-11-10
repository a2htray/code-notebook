# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QFocusEvent


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setFocus()
        app.focusChanged.connect(self.focusChangedEvent)

    def focusChangedEvent(self, event: QFocusEvent):
        print('focusChangedEvent')
        print(event, self.isActiveWindow())


if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())
