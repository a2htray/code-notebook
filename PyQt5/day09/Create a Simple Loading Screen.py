# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QTimer
from PyQt5.Qt import Qt
from PyQt5.QtGui import QMovie


class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(441, 291)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.animationLabel = QLabel(self)
        self.movie = QMovie(r'D:\private\qt-demo\assets\Loading_icon.gif')
        self.animationLabel.setMovie(self.movie)
        self.movie.start()

        timer = QTimer(self)
        timer.singleShot(3000, self.stopLoading)

    def stopLoading(self):
        self.movie.stop()
        self.close()


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel('<font size=12>This a main app window.</font>', self)
        label.setGeometry(150, 150, 400, 50)
        self.loadingScreen = LoadingScreen()
        self.show()


if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()

    sys.exit(app.exec())
