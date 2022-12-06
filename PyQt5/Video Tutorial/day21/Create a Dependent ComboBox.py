import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QComboBox


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(200)
        layout = QHBoxLayout()

        self.cbProvince = QComboBox()
        self.cbProvince.addItem('浙江省', ['杭州', '宁波'])
        self.cbProvince.addItem('湖北', ['武汉', '荆门'])
        self.cbCity = QComboBox()

        self.cbProvince.currentIndexChanged.connect(self.handleProvinceIndexChanged)

        layout.addWidget(self.cbProvince)
        layout.addWidget(self.cbCity)

        self.setLayout(layout)

        self.handleProvinceIndexChanged(self.cbProvince.currentIndex())

    def handleProvinceIndexChanged(self, index):
        self.cbCity.clear()
        cities = self.cbProvince.itemData(index)
        if cities:
            self.cbCity.addItems(cities)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
