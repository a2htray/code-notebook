import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QListWidget, QVBoxLayout, QListWidgetItem, QWidget
from PyQt5.QtCore import Qt


class ComparableListWidgetItem(QListWidgetItem):
    def __lt__(self, other):
        try:
            return float(self.text()) < float(other.text())
        except:
            return super().__lt__(other)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 600)
        layout = QVBoxLayout()
        btnAscending = QPushButton('Sort Ascending')
        btnAscending.clicked.connect(self.sortAscending)
        btnDescending = QPushButton('Sort Descending')
        btnDescending.clicked.connect(self.sortDescending)
        self.lwNumber = QListWidget()

        numbers = [1, 2, 3, 4, 10, 9, 8, 1]
        for number in numbers:
            self.lwNumber.addItem(ComparableListWidgetItem(str(number)))

        layout.addWidget(btnAscending)
        layout.addWidget(btnDescending)
        layout.addWidget(self.lwNumber, 1)
        self.setLayout(layout)

    def sortAscending(self):
        self.lwNumber.sortItems(Qt.AscendingOrder)

    def sortDescending(self):
        self.lwNumber.sortItems(Qt.DescendingOrder)


if __name__ == '__main__':
    print('aaa')
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
