# -*- coding=utf-8 -*-
r"""
"""
import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class ChangeIcon(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle('Set Icons Example')
        self.setWindowIcon(QIcon('assets/pyqt_logo.png'))  # 设置窗口图标
        self.createWidgets()
        self.show()

    def createWidgets(self):
        info_label = QLabel('Click on the button and select a fruit.')
        self.images = [
            ['apple', 'assets/1_apple.png'],
            ['pineapple', 'assets/2_pineapple.png'],
            ['watermelon', 'assets/3_watermelon.png'],
            ['banana', 'assets/4_banana.png'],
        ]
        self.icon_button = QPushButton(self)
        image = random.choice(self.images)
        self.icon_button.setIcon(QIcon(image[1]))  # 给按钮设置 Icon
        self.icon_button.setText(image[0].capitalize())
        self.icon_button.setIconSize(QSize(60, 60))
        self.icon_button.clicked.connect(self.changeButtonIcon)

        v_box = QVBoxLayout()
        v_box.addWidget(info_label)
        v_box.addWidget(self.icon_button)

        self.setLayout(v_box)

    def changeButtonIcon(self):
        image = random.choice(self.images)
        self.icon_button.setIcon((QIcon(image[1])))
        self.icon_button.setText(image[0].capitalize())
        self.icon_button.setIconSize(QSize(60, 60))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChangeIcon()
    sys.exit(app.exec())