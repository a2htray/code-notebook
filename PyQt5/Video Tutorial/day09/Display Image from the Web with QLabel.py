# -*- coding=utf-8 -*-
r"""
"""
import sys
import requests
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QPixmap, QImage

imageURL = 'https://www.baidu.com/img/pc_675fe66eab33abff35a2669768c43d95.png'


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        image = QImage()
        content = requests.get(imageURL).content
        print(content)
        image.loadFromData(requests.get(imageURL).content)

        imageLabel = QLabel()
        imageLabel.setPixmap(QPixmap(image))
        imageLabel.show()


if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())