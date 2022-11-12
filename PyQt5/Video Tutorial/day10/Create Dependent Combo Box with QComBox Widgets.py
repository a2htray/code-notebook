# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout

data = [
    ['America', ['California', 'Texas']],
    ['Canada', ['Alberta', 'British Columbia', 'Ontario']],
]


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.parentCombobox = QComboBox(self)
        self.childCombobox = QComboBox(self)

        for countryData in data:
            self.parentCombobox.addItem(countryData[0])

        layout.addWidget(self.parentCombobox)
        layout.addWidget(self.childCombobox)
        self.setLayout(layout)

        self.parentCombobox.currentIndexChanged.connect(self.changeComboboxIndex)

        self.setComboboxIndex(0)

    def setComboboxIndex(self, index: int):
        self.changeComboboxIndex(index)

    def changeComboboxIndex(self, index: int):
        print(f'current index: {index}, cities: {data[index][1:][0]}')
        self.childCombobox.clear()
        for city in data[index][1:][0]:
            self.childCombobox.addItem(city)


if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())
