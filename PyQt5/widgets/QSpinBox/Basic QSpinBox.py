# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QVBoxLayout, QGridLayout, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 250, 200)
        self.setWindowTitle('Basic QSpinBox')

        layout = QGridLayout()
        layout.addWidget(QLabel('Price'), 0, 0)

        self.sbPrice = QSpinBox(self)
        self.sbPrice.setRange(0, 100)
        self.sbPrice.setSuffix(' RMB')
        self.sbPrice.setSingleStep(10)  # 设置步长

        # textChanged 比 valueChanged 先发生 (emit)
        self.sbPrice.valueChanged.connect(self.handleValueChanged)
        self.sbPrice.textChanged.connect(self.handleTextChanged)

        layout.addWidget(self.sbPrice, 0, 1)
        self.setLayout(layout)

        self.show()

    def handleValueChanged(self, value: int):
        print(f'Value: {value}')

    def handleTextChanged(self, text: str):
        print(f'Text: {text}')





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
