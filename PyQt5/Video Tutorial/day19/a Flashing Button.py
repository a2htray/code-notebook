import sys
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import QTimer


class FlashingButton(QPushButton):
    def __init__(self):
        super().__init__('a Flashing Button')
        self.resize(100, 50)
        self.flag = True
        self.clicked.connect(lambda _: print('hello world.'))

        timer = QTimer(self, interval=1000)
        timer.timeout.connect(self.flashing)
        timer.start()
        print(self)

    def flashing(self):
        if self.flag:
            self.setStyleSheet('background-color: orange;')
        else:
            self.setStyleSheet('background-color: none;')

        self.flag = not self.flag


if __name__ == '__main__':
    print('aaa')
    app = QApplication(sys.argv)
    demo = FlashingButton()
    demo.show()
    sys.exit(app.exec())
