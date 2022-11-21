import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import QTimer


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.n = 10

        layout = QVBoxLayout()
        for i in range(self.n):
            btn = QPushButton(str(i + 1))
            btn.setObjectName(f'Button {i + 1}')
            layout.addWidget(btn)

        self.setLayout(layout)

        timer = QTimer(self, interval=1000)
        timer.timeout.connect(self.updateText)
        timer.start()

    def updateText(self):
        for i in range(self.n):
            child = self.findChild(QPushButton, f'Button {i + 1}')  # 重点
            number = int(child.text())
            child.setText(str(number + 1))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
