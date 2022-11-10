# -*- coding=utf-8 -*-
r"""
"""
import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QFont, QDragEnterEvent, QDragMoveEvent, QDropEvent
from PyQt5.Qt import Qt


class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setText('Drag and Drop')
        self.setFont(QFont('Open sans', 25))
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet('''
            QLabel {
                border: 4px dashed #aaa;
            }
        ''')

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        print('dragEnterEvent', dir(event))
        print('dragEnterEvent', event.mimeData())
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event: QDragMoveEvent) -> None:
        print('dragMoveEvent', dir(event))
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent) -> None:
        print('dropEvent', dir(event))
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            filePath = event.mimeData().urls()[0].toLocalFile()
            self.setPixmap(QPixmap(filePath))
            event.accept()
        else:
            event.ignore()


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.setAcceptDrops(True)

        layout = QVBoxLayout()
        imageLabel = ImageLabel()
        layout.addWidget(imageLabel)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())