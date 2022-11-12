# -*- coding=utf-8 -*-
r"""
@link https://www.youtube.com/watch?v=qwzapIxXRSQ&list=PL3JVwFmb_BnRpvOeIh_To4YSiebiggyXS&index=74&ab_channel=JieJenn
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout


class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=100)
        super().__init__(fig)
        self.setParent(parent)

        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t)

        self.ax.plot(t, s)
        self.ax.set(xlabel='Time (s)', ylabel='Voltage (mV)', title='Demo')


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 400)
        layout = QVBoxLayout()
        self.chart = Canvas(self)

        layout.addWidget(self.chart)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])

    demo = Demo()
    demo.show()

    sys.exit(app.exec())