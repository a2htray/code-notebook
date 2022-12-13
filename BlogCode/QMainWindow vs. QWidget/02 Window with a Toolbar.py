import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


class BasicWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Window with a Toolbar')
        toolbar = self.addToolBar('main toolbar')

        actCut = QAction('Cut', self)
        actCut.triggered.connect(lambda _: print('action cut'))
        actPaste = QAction('Paste', self)
        actPaste.triggered.connect(lambda _: print('action paste'))

        toolbar.addAction(actCut)
        toolbar.addAction(actPaste)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicWindow()
    window.show()
    sys.exit(app.exec())
