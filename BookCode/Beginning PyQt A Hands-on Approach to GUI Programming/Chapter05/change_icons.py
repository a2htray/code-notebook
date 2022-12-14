import sys
import random
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QPushButton, QVBoxLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class ChangeIcon(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle('Set Icons Example')
        self.setWindowIcon(QIcon('images/pyqt_logo.png'))  # 设置窗口左上角图标
        self.createWidgets()
        self.show()

    def createWidgets(self):
        lblInfo = QLabel('Click on the button and select a fruit')
        self.images = [
            'images/1_apple.png',
            'images/2_pineapple.png',
            'images/3_watermelon.png',
            'images/4_banana.png'
        ]

        self.btnIcon = QPushButton(self)
        self.btnIcon.setIcon(QIcon(random.choice(self.images)))  # 调用部件的 setIcon 方法可以在其之上显示 Icon
        self.btnIcon.setIconSize(QSize(60, 60))  # 设置 Icon 的大小
        self.btnIcon.clicked.connect(self.changeButtonIcon)

        blyt = QVBoxLayout()
        blyt.addWidget(lblInfo)
        blyt.addWidget(self.btnIcon)

        self.setLayout(blyt)

    def changeButtonIcon(self):
        self.btnIcon.setIcon(QIcon(random.choice(self.images)))
        self.btnIcon.setIconSize(QSize(60, 60))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChangeIcon()
    sys.exit(app.exec())
