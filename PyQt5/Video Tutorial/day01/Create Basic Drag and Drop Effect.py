# -*- coding=utf-8 -*-
r"""
文本的拖拽
"""

import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QDragEnterEvent, QDropEvent


class DragAndDropWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        edit1 = QLineEdit('', self)
        edit1.setDragEnabled(True)  # 允许拖拽
        edit1.move(20, 30)

        edit2 = QLineEdit('', self)
        edit2.setDragEnabled(False)
        edit2.move(20, 70)

        button = DragAndDropButton('&Button', self)
        button.move(200, 50)


class DragAndDropButton(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)  # 设置按钮允许拖拽

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        """拖事件"""
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent) -> None:
        """松开事件"""
        self.setText(event.mimeData().text())


def main():
    app = QApplication(sys.argv)
    widget = DragAndDropWidget()
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
