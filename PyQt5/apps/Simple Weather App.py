# -*- coding=utf-8 -*-
r"""
"""
import sys
import re
import requests
import pyqtgraph as pg
import pandas as pd
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, \
    QLineEdit, QPushButton, QAction, QActionGroup
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class City:
    def __init__(self, code, label):
        self.code = code
        self.label = label

cities = [City(code, label) for code, label in [
    (57494, '武汉'),
    (58562, '宁波'),
    (59493, '深圳'),
]]

weatherDataColumns = ['Week', 'Day', 'High Temperature', 'Low Temperature']


REGEX_WEEK_DAY = re.compile('^([\u4e00-\u9fa5]{3})(\d{2}/\d{2})$')


def extractWeekAndDay(wdString: str):
    """提取'周'和'日'信息
    >>> extractWeekAndDay('星期五11/04')
    ('星期五', '11/04')
    >>> extractWeekAndDay('not_match_pattern')
    ValueError: the string of week and day does not match the pattern
    """
    match = REGEX_WEEK_DAY.match(wdString)
    if not match:
        raise ValueError('the string of week and day does not match the pattern')

    return REGEX_WEEK_DAY.findall(wdString)[0]


def getWeatherData(cityCode: int):
    """根据城市代码获取天气数据，返回一个 DataFrame
    >>> getWeatherData('57494')
      Week    Day High Temperature Low Temperature
    0  星期一  11/07               25              10
    1  星期二  11/08               25              13
    2  星期三  11/09               26              13
    3  星期四  11/10               28              16
    4  星期五  11/11               28              16
    5  星期六  11/12               23              12
    6  星期日  11/13               13               7
    """
    df = pd.DataFrame(columns=['Week', 'Day', 'High Temperature', 'Low Temperature'])
    url = 'http://weather.cma.cn/web/weather/{0}.html'.format(cityCode)
    htmlContent = requests.get(url).content.decode('utf-8')

    soup = BeautifulSoup(htmlContent, 'html.parser')
    eleDays = soup.select('.day')

    for i, eleDay in enumerate(eleDays):
        eleDayItems = eleDay.select('.day-item')
        week, day = extractWeekAndDay(eleDayItems[0].getText().replace(' ', '').replace('\n', ''))
        highTemperature = eleDayItems[5].select('.high')[0].getText().strip().replace('℃', '')
        lowTemperature = eleDayItems[5].select('.low')[0].getText().strip().replace('℃', '')

        df.loc[i] = [week, day, highTemperature, lowTemperature]

    return df


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Weather App')
        self.resize(800, 600)
        font = QFont('Open Sans', pointSize=12)
        self.menuBar().setFont(font)
        self.menuCity = self.menuBar().addMenu('城市')
        actionGroupCity = QActionGroup(self.menuCity)

        self.menuCity.setFont(font)

        for city in cities:
            action = self.menuCity.addAction(city.label)
            action.setData(city.code)
            action.setCheckable(True)
            actionGroupCity.addAction(action)
        actionGroupCity.setVisible(True)

        actionGroupCity.triggered.connect(self.onTriggeredCity)

        self.initAppData()

    def initAppData(self):
        self.menuCity.actions()[0].setChecked(True)
        cityCode = self.getCurrentCityCode()
        print(getWeatherData(cityCode))

    def getCurrentCityCode(self):
        for action in self.menuCity.actions():
            if action.isChecked():
                return int(action.data())

    def onTriggeredCity(self, action: QAction):
        print(action.data())


if __name__ == '__main__':
    getWeatherData(57494)
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
