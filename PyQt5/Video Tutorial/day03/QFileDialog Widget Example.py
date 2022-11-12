# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QFileDialog, QBoxLayout, QTextEdit, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir


class FileDialogDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.button1 = QPushButton('Upload Image')
        self.button1.clicked.connect(self.getImageFile)
        self.labelImage = QLabel()
        self.button2 = QPushButton('Upload File')
        self.button2.clicked.connect(self.getTextFile)
        self.textEditor = QTextEdit()

        layout = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addWidget(self.button1)
        layout.addWidget(self.labelImage)
        layout.addWidget(self.button2)
        layout.addWidget(self.textEditor)

        self.setLayout(layout)

    def getImageFile(self):
        file, _ = QFileDialog.getOpenFileName()
        self.labelImage.setPixmap(QPixmap(file))

    def getTextFile(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            file: str = dialog.selectedFiles()[0]
            if file.endswith('.py'):
                with open(file, 'r') as f:
                    data = f.read()
                    self.textEditor.setPlainText(data)
                    f.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = FileDialogDemo()
    demo.show()

    sys.exit(app.exec_())
