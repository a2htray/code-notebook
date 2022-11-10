# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QToolBox, QGridLayout, QBoxLayout, QLabel, \
    QPushButton, QTextEdit, QLineEdit
from PyQt5.QtGui import QColor


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 400)
        self.resize(600, 400)
        layout = QGridLayout()

        styleSheet = """
            QToolBox::tab {
                border: 1px solid #CCCCCC;
                border-bottom-color: #9E9E9E;
            }
            QToolBox::tab::selected {
                background-color: #F14040;
                border-bottom-style: none;
            }
        """

        self.toolBox = QToolBox()
        layout.addWidget(self.toolBox, 0, 0)

        w1 = QWidget()
        layout1 = QBoxLayout(QBoxLayout.LeftToRight)
        layout1.addWidget(QLabel('Enter something'))
        layout1.addWidget(QLineEdit())
        w1.setLayout(layout1)
        self.toolBox.addItem(w1, 'Tab 1')

        w2 = QWidget()
        layout2 = QBoxLayout(QBoxLayout.LeftToRight)
        layout2.addWidget(QLabel('Enter something'))
        layout2.addWidget(QLineEdit())
        w2.setLayout(layout2)
        self.toolBox.addItem(w2, 'Tab 2')

        self.toolBox.setStyleSheet(styleSheet)
        self.toolBox.setCurrentIndex(1)
        self.toolBox.setItemToolTip(0, 'this is Tab 1')
        self.toolBox.setItemToolTip(1, 'this is Tab 2')
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec_())