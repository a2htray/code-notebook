# -*- coding=utf-8 -*-
# QHBoxLayout is one of the two box layouts in PyQt

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
)
from PyQt5.Qt import (
    Qt,
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QHBoxLayout Example')

        layout = QVBoxLayout()

        # layout.addWidget 的第 2 参数是伸展因子
        # 当窗口大小改变时，不同 Widget 响应的 Widget 大小
        # 第 3 个参数指定 Widget 的位置
        layout.addWidget(QPushButton('Top-Most'))
        layout.addWidget(QPushButton('Center'), 1)
        layout.addWidget(QPushButton('Bottom-Most'), 2)
        layout.addStretch()

        self.setLayout(layout)

        print(self.children())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

