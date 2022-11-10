# -*- coding=utf-8 -*-
r"""
使用 QIcon
"""

import sys
from PyQt5.QtWidgets import QWidget, QComboBox, QApplication
from PyQt5.QtGui import QIcon

if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = QWidget()
    widget.resize(400, 400)

    combo = QComboBox(widget)
    combo.resize(100, 20)
    combo.move(100, 50)
    combo.addItem(QIcon(r'D:\private\qt-demo\assets\Banana.png'), 'Banana')
    combo.addItem(QIcon(r'D:\private\qt-demo\assets\Orange.png'), 'Orange')

    widget.show()

    sys.exit(app.exec_())


