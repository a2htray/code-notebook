import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        mainLayout = QHBoxLayout()

        btnA = QPushButton('in Layout A')
        btnA.clicked.connect(self.iterateLayout)
        lineEdit0 = QLineEdit()
        lineEdit1 = QLineEdit()

        self.layoutA = QVBoxLayout()
        self.layoutA.addWidget(btnA)
        self.layoutA.addWidget(lineEdit0)
        self.layoutA.addWidget(lineEdit1)

        btnB = QPushButton('in Layout B')
        btnB.clicked.connect(self.iterateLayout)
        lineEdit2 = QLineEdit()
        lineEdit3 = QLineEdit()

        self.layoutB = QVBoxLayout()
        self.layoutB.addWidget(btnB)
        self.layoutB.addWidget(lineEdit2)
        self.layoutB.addWidget(lineEdit3)

        mainLayout.addLayout(self.layoutA)
        mainLayout.addLayout(self.layoutB)

        self.setLayout(mainLayout)

    def iterateLayout(self):
        sender = self.sender()
        if sender.text() == 'in Layout A':
            layout = self.layoutA
        else:
            layout = self.layoutB

        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if isinstance(widget, QLineEdit):
                print(widget.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
