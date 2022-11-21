import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QCheckBox


class Window(QWidget):
    def __init__(self):
        super().__init__()
        items = [f'item {i}' for i in range(110)]

        layout = QGridLayout()

        for i, item in enumerate(items):
            checkbox = QCheckBox(item)
            checkbox.clicked.connect(self.toggleCheckBox)
            layout.addWidget(checkbox, i // 4, i % 4)

        self.setLayout(layout)

    def toggleCheckBox(self):
        sender = self.sender()
        if isinstance(sender, QCheckBox):
            print(sender.isChecked(), sender.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
