# -*- coding=utf-8 -*-
r"""
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLCDNumber, QBoxLayout
from PyQt5.Qt import Qt


class LCDNumberDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 500)
        self.setWindowTitle('Update LCD with Slider')

        self.lcd = QLCDNumber()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

        self.slider.valueChanged.connect(self.updateLCD)

        layout = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addWidget(self.lcd)
        layout.addWidget(self.slider)

        self.setLayout(layout)

    def updateLCD(self, event):
        self.lcd.display(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = LCDNumberDemo()
    demo.show()

    sys.exit(app.exec_())
