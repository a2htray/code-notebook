# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.setWindowOpacity(0.7)
    widget.show()

    sys.exit(app.exec_())
