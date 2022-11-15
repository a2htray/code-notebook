# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QGridLayout, QPushButton


class ShowInputDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle('How to Show a Input Dialog')

        layout = QGridLayout()
        self.btn00 = QPushButton('00')
        self.btn00.clicked.connect(lambda _: print(QInputDialog.getText(self, '00 Text', 'Text:')))
        self.btn01 = QPushButton('01')
        self.btn01.clicked.connect(lambda _: print(QInputDialog.getInt(self, '01 Int', 'Int:')))
        self.btn10 = QPushButton('10')
        self.btn10.clicked.connect(lambda _: print(QInputDialog.getDouble(self, '10 Double', 'Double:')))
        self.btn11 = QPushButton('11')
        self.btn11.clicked.connect(lambda _: print(QInputDialog.getItem(self, '11 Item', 'Item:', ['a', 'b', 'c'])))

        # QInputDialog.getMultiLineText

        layout.addWidget(self.btn00, 0, 0)
        layout.addWidget(self.btn01, 0, 1)
        layout.addWidget(self.btn10, 1, 0)
        layout.addWidget(self.btn11, 1, 1)
        self.setLayout(layout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShowInputDialog()
    sys.exit(app.exec())
