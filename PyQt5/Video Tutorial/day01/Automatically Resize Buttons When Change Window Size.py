# -*- coding=utf-8 -*-
r"""
自适应按钮大小
"""

import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QSizePolicy, QApplication, QPushButton


class GridDemo(QWidget):
    def __init__(self):
        super().__init__()
        values = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
        ]

        positions = [(r, c) for r in range(3) for c in range(3)]
        gridLayout = QGridLayout()

        self.setLayout(gridLayout)

        for positions, value in zip(positions, values):
            button = QPushButton(value)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 自适应大小的关键
            gridLayout.addWidget(button, *positions)


def main():
    app = QApplication(sys.argv)

    demo = GridDemo()
    demo.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
