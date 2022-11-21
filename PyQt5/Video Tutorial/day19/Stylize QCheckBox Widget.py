import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QHBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stylize QCheckBox')

        layout = QHBoxLayout()

        self.setStyleSheet('''
            QCheckBox {
                font-size: 40px;
                color: orange;
            }
            QCheckBox::indicator {
                width: 30px;
                height: 30px;
            }
        ''')

        cbYes = QCheckBox('Yes')
        cbNo = QCheckBox('No')
        layout.addWidget(cbYes)
        layout.addWidget(cbNo)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
