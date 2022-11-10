# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont


class DemoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Progress Bar Demo')
        self.resize(500, 100)

        font = QFont('Open sans', 18, italic=True)
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(25, 25, 300, 40)
        self.progressBar.setMaximum(250)
        self.progressBar.setValue(0)
        self.progressBar.setFont(font)

        # %p - is replaced by the percentage completed.
        # %v - is replaced by the current value.
        # %m - is replaced by the total number of steps
        self.progressBar.setFormat('%v of %m')

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.increaseStep)
        self.timer.start(1000)

    def increaseStep(self, *args):
        if int(self.progressBar.value()) == 250:
            self.timer.stop()
        self.progressBar.setValue(self.progressBar.value() + 250.0/100)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    demo = DemoApp()
    demo.show()
    sys.exit(app.exec())
