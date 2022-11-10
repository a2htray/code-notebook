# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QDrag, QPainter, QPixmap, QMouseEvent, QDropEvent, QDragEnterEvent
from PyQt5.QtCore import Qt, QMimeData, QEvent


class DragLabel(QLabel):
    # def mousePressEvent(self, event: QMouseEvent) -> None:
    #     print(event.pos())
    #     return
    #     if event.button() == Qt.LeftButton:
    #         self.drag_start_pos = event.pos()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        print('mouseMoveEvent')
        if not (event.buttons() & Qt.LeftButton):
            return
        else:
            drag = QDrag(self)
            mimeData = QMimeData()
            mimeData.setText(self.text())
            drag.setMimeData(mimeData)

            print(self.grab())
            pixmap = QPixmap(self.size())
            painter = QPainter(pixmap)
            painter.drawPixmap(self.rect(), self.grab())
            painter.end()

            drag.setPixmap(pixmap)
            drag.setHotSpot(event.pos())
            drag.exec(Qt.CopyAction | Qt.MoveAction)


class DropLabel(QLabel):
    def __init__(self, label, parent):
        super().__init__(label, parent)
        # 允许拖拽
        self.setAcceptDrops(True)

    def dropEvent(self, event: QDropEvent) -> None:
        """松开鼠标左键"""
        text = event.mimeData().text()
        self.setText(text)

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        """"""
        print(event.mimeData().text(), event.mimeData().hasText())
        if event.mimeData().hasText():
            event.acceptProposedAction()


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        labelToDrag = DragLabel('X', self)
        labelToDrop = DropLabel('Y', self)

        labelToDrop.move(50, 50)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())
