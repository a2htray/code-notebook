# -*- coding=utf-8 -*-
r"""
QLabel 可以用来显示图片
1. QPixmap(image)
2. QLabel.setPixmap(pixmap)

QtGui 模块包含很多处理图像的元素，比如 QPixmap

.move() 即使用了绝对定位
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap


class HelloWorldWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle('QLabel Example')
        self.displayLabels()
        self.show()

    def displayLabels(self):
        text = QLabel(self)
        text.setText('Hello')
        text.move(105, 15)

        image = r'D:\private\code-notebook\PyQt5\assets\Banana.png'
        try:
            with open(image):
                worldImage = QLabel(self)
                pixmap = QPixmap(image)
                worldImage.setPixmap(pixmap)
                worldImage.move(25, 40)
        except FileNotFoundError:
            print('Image not found')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HelloWorldWindow()
    # .exec() 开启事件轮询
    sys.exit(app.exec())

        