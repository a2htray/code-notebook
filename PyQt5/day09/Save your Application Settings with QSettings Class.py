# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.Qt import QSettings
from PyQt5.QtGui import QCloseEvent


class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.settings = QSettings('PyQt5', 'demo', self)

        try:
            self.resize(self.settings.value('window size'))
            self.move(self.settings.value('window position'))
        except:
            pass

    def closeEvent(self, event: QCloseEvent) -> None:
        self.settings.setValue('window size', self.size())
        self.settings.setValue('window position', self.pos())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())
