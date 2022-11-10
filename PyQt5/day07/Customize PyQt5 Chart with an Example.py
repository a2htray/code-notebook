# -*- coding=utf-8 -*-
r"""
"""
import random
import sys
from typing import Tuple
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QCategoryAxis
from PyQt5.QtCore import QPoint
from PyQt5.Qt import QPen, QFont, Qt, QSize
from PyQt5.QtGui import QColor, QBrush, QLinearGradient, QGradient, QPainter


class Demo(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置窗口标题
        self.setWindowTitle('Chart Formatting Demo')
        # 设置窗口大小
        self.resize(1200, 800)
        self.initChart()

        self.setCentralWidget(self.chartView)

    def initChart(self):
        self.series = self.createLineSeries()
        chart = QChart()
        chart.legend().hide()
        chart.addSeries(self.series)

        # 设置标题字体
        font = QFont('Open sans')
        font.setPixelSize(40)
        font.setBold(True)
        chart.setTitleFont(font)
        # 设置标题颜色
        chart.setTitleBrush(QBrush(Qt.yellow))
        chart.setTitle('Custom Chart Demo')

        # 设置 chart 背景色
        backgroundGradient = QLinearGradient()
        backgroundGradient.setStart(QPoint(0, 0))
        backgroundGradient.setFinalStop(QPoint(0, 1))
        backgroundGradient.setColorAt(0.0, QColor(175, 201, 182))
        backgroundGradient.setColorAt(1.0, QColor(51, 105, 66))
        backgroundGradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        chart.setBackgroundBrush(backgroundGradient)

        # 设置 plot 背景色
        plotAreaGradient = QLinearGradient()
        plotAreaGradient.setStart(QPoint(0, 1))
        plotAreaGradient.setFinalStop(QPoint(1, 0))
        plotAreaGradient.setColorAt(0.0, QColor(222, 222, 222))
        plotAreaGradient.setColorAt(1.0, QColor(51, 105, 66))
        plotAreaGradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        chart.setPlotAreaBackgroundBrush(plotAreaGradient)
        chart.setPlotAreaBackgroundVisible(True)

        axisX, axisY = self.createAxisXY()
        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)

        self.series.attachAxis(axisX)
        self.series.attachAxis(axisY)

        self.chartView = QChartView(chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)

    def createLineSeries(self) -> QLineSeries:
        n = 10
        series = QLineSeries()

        # 给线条设置样式
        pen = QPen(QColor(200, 200, 200))
        pen.setWidth(5)
        series.setPen(pen)

        for i in range(n):
            series.append(i, random.randint(0, 15))
        return series

    def createAxisXY(self) -> Tuple[QCategoryAxis, QCategoryAxis]:
        axisX = QCategoryAxis()
        axisY = QCategoryAxis()

        # 字体
        labelFont = QFont('Open Sans')
        labelFont.setPixelSize(25)

        axisX.setLabelsFont(labelFont)
        axisY.setLabelsFont(labelFont)

        # 轴颜色
        axisPen = QPen(Qt.white)
        axisPen.setWidth(2)
        axisX.setLinePen(axisPen)
        axisY.setLinePen(axisPen)

        # label 颜色
        axixBrush = QBrush(Qt.white)
        axisX.setLabelsBrush(axixBrush)
        axisY.setLabelsBrush(axixBrush)

        axisX.setRange(0, 10)
        axisX.append('slow', 0)
        axisX.append('average', 5)
        axisX.append('fast', 10)

        axisY.setRange(0, 15)
        axisY.append('low', 0)
        axisY.append('medium', 8)
        axisY.append('high', 15)

        axisX.setGridLineVisible(False)
        axisY.setGridLineVisible(False)

        return axisX, axisY


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
