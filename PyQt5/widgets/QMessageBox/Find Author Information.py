# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QMessageBox, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt


class DisplayMessageBox(QWidget):
    def __init__(self):
        super().__init__()
        self.loadAuthors()
        self.initializeUI()

    def loadAuthors(self):
        self.authors = [author.strip() for author in open('./assets/authors.txt').readlines()]

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('QMessageBox Example')
        self.displayWidgets()
        self.show()

    def displayWidgets(self):
        catalogueLabel = QLabel('Author Catalogue', self)
        catalogueLabel.setGeometry(0, 10, 400, 30)
        catalogueLabel.setAlignment(Qt.AlignCenter)
        catalogueLabel.setFont(QFont('Arial', 20))

        authLabel = QLabel('Enter the name of the author you are searching for:', self)
        authLabel.setGeometry(0, 50, 400, 30)
        authLabel.setAlignment(Qt.AlignCenter)

        self.authEntry = QLineEdit(self)
        self.authEntry.setPlaceholderText('enter author name')
        self.authEntry.setGeometry(100, 90, 200, 30)

        self.searchButton = QPushButton('Search', self)
        self.searchButton.setGeometry(150, 140, 100, 30)
        self.searchButton.clicked.connect(self.handleSearchAuthor)

    def handleSearchAuthor(self):
        print('DisplayMessageBox.handleSearchAuthor')
        authorPattern = self.authEntry.text().strip()
        self.authEntry.setText(authorPattern)

        foundAuthors = []
        for author in self.authors:
            if authorPattern in author:
                foundAuthors.append(author)

        if len(foundAuthors) != 0:
            QMessageBox.information(self, 'Author Found', '\n'.join(foundAuthors), QMessageBox.Ok, QMessageBox.Ok)
        else:
            notFoundMessageResponse = QMessageBox.question(self, 'Author Not Found',
                                                           'Author not found in catalogue.\nDo you wish to continue?',
                                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if notFoundMessageResponse == QMessageBox.No:
                self.close()
            else:
                pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DisplayMessageBox()
    sys.exit(app.exec())


