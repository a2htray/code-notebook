# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout
from PyQt5.QtGui import QTextCursor


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        layout = QVBoxLayout()

        self.textEdit = QTextEdit()
        self.textEdit.acceptDrops()
        layout.addWidget(self.textEdit)

        document = self.textEdit.document()
        cursor = QTextCursor(document)

        cursor.insertImage(r'D:\private\code-notebook\PyQt5\assets\Banana.png')
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())
