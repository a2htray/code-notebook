# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QMouseEvent, QDragMoveEvent, QDragEnterEvent, QDropEvent


class Button(QPushButton):
    def __init__(self, text, parent):
        super().__init__(text, parent)
        self.setStyleSheet('font-size: 20px; width: 50px; height: 25px;')

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        print('Button.mouseMoveEvent')
        if event.buttons() == Qt.LeftButton:
            mimeData = QMimeData()
            mimeData.setData('type', b'buttonMove')
            # mimeData.setData()
            drag = QDrag(self)
            drag.setMimeData(mimeData)
            dropAction = drag.exec(Qt.MoveAction)


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 400)
        self.setAcceptDrops(True)
        self.button = Button('Drag Me', self)

        self.mouseXY = {
            'x': 0,
            'y': 0,
        }

        self.buttonXY = {
            'x': 0,
            'y': 0,
        }

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        print('AppDemo.dragEnterEvent')
        self.mouseXY = {
            'x': event.pos().x(),
            'y': event.pos().y(),
        }
        self.buttonXY = {
            'x': self.button.pos().x(),
            'y': self.button.pos().y(),
        }
        event.accept()

    def dragMoveEvent(self, event: QDragMoveEvent) -> None:
        print('AppDemo.dragMoveEvent')
        print(event.mimeData().data('type'))
        print(type(event.mimeData().sender()))
        position = event.pos()

        x = position.x() - self.mouseXY['x'] + self.buttonXY['x']
        y = position.y() - self.mouseXY['y'] + self.buttonXY['y']

        self.button.move(x, y)
        event.accept()

    def dropEvent(self, event: QDropEvent) -> None:
        print('AppDemo.dropEvent')
        # position = event.pos()
        # self.button.move(position)
        # event.accept()


if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())