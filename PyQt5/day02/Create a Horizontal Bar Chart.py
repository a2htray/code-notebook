# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QChartView, QHorizontalBarSeries, QBarSet, QBarCategoryAxis, QValueAxis
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        set0 = QBarSet('X0')
        set1 = QBarSet('X1')
        set2 = QBarSet('X2')
        set3 = QBarSet('X3')
        set4 = QBarSet('X4')

        set0.append([1, 4, 1, 4])
        set1.append([4, 1, 3, 2])
        set2.append([2, 2, 4, 4])
        set3.append([5, 4, 3, 9])
        set4.append([1, 6, 6, 7])

        series = QHorizontalBarSeries()
        series.append([set0, set1, set2, set3, set4])
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Horizontal Bar Chart')

        chart.setAnimationOptions(QChart.SeriesAnimations)

        months = ('一月', '二月', '三月', '四月')

        axisY = QBarCategoryAxis()
        axisY.append(months)
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

        axisX = QValueAxis()
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)
        axisX.applyNiceNumbers()

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignLeft)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartView)
        self.setWindowTitle('Horizontal Bar Chart')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())