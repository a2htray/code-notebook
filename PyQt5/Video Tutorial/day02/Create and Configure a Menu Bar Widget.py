# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


class MenuBarDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Bar Demo')
        self.resize(800, 600)
        self.menuBar = self.menuBar()

        fileMenu = self.menuBar.addMenu('File')
        exitAction = QAction('Exit App', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(lambda _: QApplication.quit())
        fileMenu.addAction(exitAction)

        editMenu = self.menuBar.addMenu('Edit')
        undoDeleteMenu = editMenu.addMenu('Undo Delete')

        yesAction = QAction('yes', self)
        yesAction.triggered.connect(lambda _: print('yes'))
        noAction = QAction('no', self)
        noAction.triggered.connect(lambda _: print('no'))

        undoDeleteMenu.addAction(yesAction)
        undoDeleteMenu.addAction(noAction)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MenuBarDemo()
    demo.show()
    sys.exit(app.exec_())
