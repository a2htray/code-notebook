# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QMainWindow, QAction
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt, QTimer, QEvent


class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 400)
        font = QFont('Open sans', 12)
        toolbar = self.addToolBar('Toolbar')
        toolbar.setFont(font)

        toolbar.setMinimumHeight(50)

        startAction: QAction = toolbar.addAction('Start')
        startAction.setCheckable(True)
        startAction.triggered.connect(self.startSlider)
        pauseAction: QAction = toolbar.addAction('Pause')
        pauseAction.setCheckable(True)
        pauseAction.triggered.connect(self.pauseSlider)
        stopAction = toolbar.addAction('Stop')
        stopAction.setCheckable(True)
        stopAction.triggered.connect(self.stopSlider)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.sliderValueChanged)
        toolbar.addWidget(self.slider)

        self.timer = QTimer()

    def startSlider(self, checked):
        print(f'start slider: {checked}')

    def pauseSlider(self, checked):
        print(f'pause slider {checked}')

    def stopSlider(self, checked):
        print(f'stop slider {checked}')

    def sliderValueChanged(self, value):
        print(value)


if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())


