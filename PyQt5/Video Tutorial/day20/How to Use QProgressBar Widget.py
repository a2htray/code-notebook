import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QVBoxLayout
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Control Progress Bar')
        layout = QVBoxLayout()

        n = 200

        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, n)
        self.progressBar.minimumSizeHint()
        self.progressBar.valueChanged.connect(lambda _: self.handleValueChanged(n))

        btnGo = QPushButton('Go', self)

        btnGo.clicked.connect(lambda status: self.run(n))

        layout.addWidget(self.progressBar)
        layout.addWidget(btnGo)

        self.setLayout(layout)

    def run(self, n):
        for i in range(n):
            time.sleep(0.01)
            self.progressBar.setValue(i+1)

    def handleValueChanged(self, n):
        if self.progressBar.value() == n:
            print('Complete!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
