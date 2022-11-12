# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime, Qt


class DemoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(450, 150)
        layout = QVBoxLayout()

        font = QFont('Open sans', 120, QFont.Bold)
        self.label = QLabel()
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.setLayout(layout)

        timer = QTimer(self)
        timer.timeout.connect(self.updateDatetime)
        timer.start(1000)

    def updateDatetime(self):
        timeText = QTime.currentTime().toString('hh:mm:ss')
        self.label.setText(timeText)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    demo = DemoApp()
    demo.show()
    sys.exit(app.exec())
