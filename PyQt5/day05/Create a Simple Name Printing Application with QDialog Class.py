# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QApplication, QBoxLayout


class Demo(QDialog):
    def __init__(self):
        super().__init__()

        self.edit = QLineEdit('Your name')
        self.edit.selectAll()

        self.button = QPushButton('Greeting')
        self.button.clicked.connect(lambda _: print(f'Hello {self.edit.text()}'))

        layout = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
