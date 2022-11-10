# -*- coding=utf-8 -*-
r"""
应用窗口保持在电脑屏幕中央
"""
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.keepCenter()

    def keepCenter(self):
        fgry = self.frameGeometry()
        print(fgry.x(), fgry.y())

        cp = QDesktopWidget().availableGeometry().center()
        print(cp.x(), cp.y())

        fgry.moveCenter(cp)
        self.move(fgry.topLeft())


def main():
    app = QApplication(sys.argv)

    demo = Demo()
    demo.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
