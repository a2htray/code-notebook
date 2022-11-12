# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QCloseEvent


class Demo(QWidget):
    def __init__(self):
        super().__init__()

    def closeEvent(self, event: QCloseEvent) -> None:
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = Demo()
    demo.show()

    sys.exit(app.exec_())
