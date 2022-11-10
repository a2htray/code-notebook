# -*- coding=utf-8 -*-
r"""
创建进度条
"""

import sys
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
from PyQt5.QtCore import QBasicTimer


class ProgressBarDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(30, 40, 200, 25)  # 设置位置、长度及高度

        self.btnStart = QPushButton('Start', self)
        self.btnStart.move(30, 80)  # 设置位置
        self.btnStart.clicked.connect(self.startProgress)  # 注册点击事件

        self.btnReset = QPushButton('Reset', self)
        self.btnReset.move(120, 80)
        self.btnReset.clicked.connect(self.resetProgress)  # 注册点击事件

        self.timer = QBasicTimer()
        self.step = 0

    def startProgress(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btnStart.setText('Start')
        else:
            self.timer.start(100, self)
            self.btnStart.setText('Stop')

    def resetProgress(self):
        self.step = 0
        self.progressBar.setValue(self.step)
        self.btnStart.setText('Start')
        if self.timer.isActive():
            self.timer.stop()

    def timerEvent(self, event) -> None:
        if self.step >= 100:
            self.timer.stop()
            self.btnStart.setText('Start')
            return
        self.step += 1
        self.progressBar.setValue(self.step)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = ProgressBarDemo()
    demo.show()

    sys.exit(app.exec_())
