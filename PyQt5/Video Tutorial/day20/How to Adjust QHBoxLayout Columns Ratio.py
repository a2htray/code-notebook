import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPlainTextEdit


class Window(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.addWidget(QPlainTextEdit(), 1)
        layout.addWidget(QPlainTextEdit(), 2)
        layout.addWidget(QPlainTextEdit(), 7)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())