# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QCheckBox, QWidget
from PyQt5.Qt import Qt


class CheckBoxWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle('QCheckBox Widget')
        self.displayCheckBoxes()

        self.show()

    def displayCheckBoxes(self):
        headerLabel = QLabel(self)
        headerLabel.setText('Which shifts can you work? (Please check all that apply)')
        headerLabel.setWordWrap(True)
        headerLabel.move(10, 10)
        headerLabel.resize(230, 60)

        for i, text in enumerate(['Morning [8 AM-2 PM]', 'Afternoon [1 PM-8 PM]', 'Night [7 PM-3 AM]']):
            checkbox = QCheckBox(text, self)
            checkbox.move(10, 80 + i * 20)
            checkbox.stateChanged.connect(self.handleStateChanged)

    def handleStateChanged(self, state):
        sender = self.sender()
        if state == Qt.Checked:
            print(f'{sender.text()} Selected')
        else:
            print(f'{sender.text()} Deselected')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CheckBoxWindow()
    sys.exit(app.exec())
