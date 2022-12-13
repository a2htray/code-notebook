import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget
from PyQt5.QtCore import Qt


class BasicWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Window with a Dock Widget')
        dockWidget = QDockWidget('a DockWidget Instance')
        self.addDockWidget(Qt.LeftDockWidgetArea, dockWidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicWindow()
    window.show()
    sys.exit(app.exec())
