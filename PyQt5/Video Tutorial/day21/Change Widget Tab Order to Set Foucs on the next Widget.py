import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QGroupBox, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        groupBox = QGroupBox('My GroupBox')
        layout.addWidget(groupBox)

        groupBoxLayout = QVBoxLayout()
        groupBox.setLayout(groupBoxLayout)

        checkboxes = []

        for i, label in enumerate([f'checkbox_{i}' for i in range(4)]):
            checkbox = QCheckBox(label)
            checkboxes.append(checkbox)
            groupBoxLayout.addWidget(checkbox)

        for i in range(len(checkboxes)):
            self.setTabOrder(checkboxes[i], checkboxes[i-1])




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
