# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.Qt import QApplication, QWidget, QIcon, QSystemTrayIcon, QMenu


class DemoApp(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    trayIcon = QSystemTrayIcon(QIcon(r'/assets/icons8-national-park-64.png'), app)
    trayIcon.setToolTip('Tray Icon')
    trayIcon.show()

    menu = QMenu()
    exitAction = menu.addAction('Exit')
    exitAction.triggered.connect(app.quit)

    trayIcon.setContextMenu(menu)

    sys.exit(app.exec())
