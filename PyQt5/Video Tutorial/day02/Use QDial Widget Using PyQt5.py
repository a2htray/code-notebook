# -*- coding=utf-8 -*-
r"""
"""
import sys

from PyQt5.QtWidgets import QApplication, QDial, QWidget, QLabel, QBoxLayout
from PyQt5.QtGui import QFont


class QDialWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dial Demo')
        self.setGeometry(100, 100, 400, 300)

        self.dial = QDial()
        self.dial.setMaximum(100)
        self.dial.setMinimum(0)
        self.dial.setValue(50)
        self.dial.valueChanged.connect(self.dialChangedEvent)

        self.label = QLabel('Dial Value is' + str(self.dial.value()))
        self.label.setFont(QFont('Open Sans', 15))

        self.layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.layout.addWidget(self.dial)
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

    def dialChangedEvent(self, value):
        print(type(value))
        self.label.setText('Dial Value is ' + str(value))


def main():
    app = QApplication(sys.argv)
    widget = QDialWidget()
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
