# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QButtonGroup, QVBoxLayout, QHBoxLayout, \
    QAbstractButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class SurveyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Survey GUI')

        mainLayout = QVBoxLayout()

        # Title
        lotTitle = QHBoxLayout()
        lotTitle.addStretch()
        lbTitle = QLabel('Restaurant')
        lbTitle.setFont(QFont('Arial', 17))
        lotTitle.addWidget(lbTitle)
        lotTitle.addStretch()
        mainLayout.addLayout(lotTitle)
        mainLayout.addStretch(1)

        # Question
        lbQuestion = QLabel('How would you rate your service today?')
        mainLayout.addWidget(lbQuestion)
        mainLayout.addStretch(1)

        # Answer
        lotAnswer = QHBoxLayout()
        cbAnswer0 = QCheckBox('Not Satisfied')
        cbAnswer1 = QCheckBox('Average')
        cbAnswer2 = QCheckBox('Satisfied')
        lotAnswer.addWidget(cbAnswer0)
        lotAnswer.addWidget(cbAnswer1)
        lotAnswer.addWidget(cbAnswer2)
        mainLayout.addLayout(lotAnswer)
        mainLayout.addStretch(4)

        bgrp = QButtonGroup(self)
        bgrp.addButton(cbAnswer0)
        bgrp.addButton(cbAnswer1)
        bgrp.addButton(cbAnswer2)

        bgrp.buttonClicked.connect(self.handleAnswerClicked)

        self.setLayout(mainLayout)

        self.show()

    def handleAnswerClicked(self, button: QAbstractButton):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SurveyWindow()
    sys.exit(app.exec())
