import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class BasicWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Window with a Status Bar')
        statusBar = self.statusBar()
        statusBar.showMessage('loading ...')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicWindow()
    window.show()
    sys.exit(app.exec())
