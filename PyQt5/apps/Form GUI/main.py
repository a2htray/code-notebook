# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFormLayout, QLineEdit, \
    QTextEdit, QSpinBox, QComboBox, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class GetAppForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('Application Form GUI')
        self.formWidgets()
        self.show()

    def formWidgets(self):
        lbTitle = QLabel('Appointment Submission Form')
        lbTitle.setFont(QFont('Arial', 18))
        lbTitle.setAlignment(Qt.AlignCenter)

        ledtName = QLineEdit()
        ledtName.resize(100, 100)
        ledtAddress = QLineEdit()
        ledtMobile = QLineEdit()
        ledtMobile.setInputMask('000-000-0000;')

        lbAge = QLabel('Age')
        sbAge = QSpinBox()
        sbAge.setRange(1, 110)
        lbHeight = QLabel('Height')
        ledtHeight = QLineEdit()
        ledtHeight.setPlaceholderText('cm')
        lbWeight = QLabel('Weight')
        ledtWeight = QLineEdit()
        ledtWeight.setPlaceholderText('kg')

        cbbGender = QComboBox()
        cbbGender.addItems(['Male', 'Female'])

        tedtSurgery = QTextEdit()
        tedtSurgery.setPlaceholderText('separate by ","')
        cbbBloodType = QComboBox()
        cbbBloodType.addItems(['A', 'B', 'AB', 'O'])

        sbHours = QSpinBox()
        sbHours.setRange(1, 12)
        cbbMinutes = QComboBox()
        cbbMinutes.addItems([':00', ':15', ':30', ':45'])
        cbbAmPm = QComboBox()
        cbbAmPm.addItems(['AM', 'PM'])

        btnSubmit = QPushButton('Submit Appointment')
        btnSubmit.clicked.connect(self.close)

        h_box = QHBoxLayout()
        h_box.addSpacing(10)
        h_box.addWidget(lbAge)
        h_box.addWidget(sbAge)
        h_box.addWidget(lbHeight)
        h_box.addWidget(ledtHeight)
        h_box.addWidget(lbWeight)
        h_box.addWidget(ledtWeight)

        desired_time_h_box = QHBoxLayout()
        desired_time_h_box.addSpacing(10)
        desired_time_h_box.addWidget(sbHours)
        desired_time_h_box.addWidget(cbbMinutes)
        desired_time_h_box.addWidget(cbbAmPm)

        app_form_layout = QFormLayout()
        app_form_layout.addRow(lbTitle)
        app_form_layout.addRow('Full Name', ledtName)
        app_form_layout.addRow('Address', ledtAddress)
        app_form_layout.addRow('Mobile Number', ledtMobile)
        app_form_layout.addRow(h_box)
        app_form_layout.addRow('Gender', cbbGender)
        app_form_layout.addRow('Past Surgeries', tedtSurgery)
        app_form_layout.addRow('Blood Type', cbbBloodType)
        app_form_layout.addRow('Desired Time', desired_time_h_box)
        app_form_layout.addRow(btnSubmit)

        self.setLayout(app_form_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GetAppForm()
    sys.exit(app.exec())
