# -*- coding=utf-8 -*-
r"""
"""
import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Window(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText('Launch Chart')
        self.clicked.connect(self.handleClicked)

    def handleClicked(self):
        print('Window.handleClick')
        fig, (ax) = plt.subplots(1, 1)
        ax.plot(range(0, 10), range(10, 0, -1))
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
