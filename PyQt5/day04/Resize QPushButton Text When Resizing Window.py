# -*- coding=utf-8 -*-
r"""
自适应按钮大小
"""

import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QSizePolicy, QApplication, QPushButton
from PyQt5.QtGui import QResizeEvent, QFont


class GridDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.values = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
        ]
        self.positions = [(r, c) for r in range(3) for c in range(3)]

        self.buttons = {}

        print(self.rect().size())

        gridLayout = QGridLayout()

        self.setLayout(gridLayout)
        for position, value in zip(self.positions, self.values):
            self.buttons[position] = QPushButton(value)
            self.buttons[position].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 自适应大小的关键
            self.buttons[position].resizeEvent = self.resizeText
            # print(self.buttons[position].font().pointSize(), self.buttons[position].height())
            gridLayout.addWidget(self.buttons[position], *position)

    def resizeText(self, event: QResizeEvent):
        for button in self.buttons.values():
            fontSize = min(button.size().width(), button.size().height())
            button.setFont(QFont('', fontSize))


def main():
    app = QApplication(sys.argv)

    demo = GridDemo()
    demo.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



