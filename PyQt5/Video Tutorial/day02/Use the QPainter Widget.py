# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap, QPainter, QPen, QPaintEvent

imagePath = r'D:\private\qt-demo\assets\Banana.png'


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.image = QPixmap(imagePath)

    def paintEvent(self, event: QPaintEvent):
        """Widget 打开事件"""
        print(event.rect())

        pen = QPen()
        pen.setWidth(5)

        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.image)
        painter.setPen(pen)
        painter.drawEllipse(10, 10, 100, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

