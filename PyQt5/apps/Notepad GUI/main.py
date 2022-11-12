# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt


class NotepadWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('Notepad GUI')

        self.renderWidgets()

        self.show()

    def renderWidgets(self):
        btnNew = QPushButton('New', self)
        btnNew.move(10, 20)
        btnNew.clicked.connect(self.clearContent)

        btnSave = QPushButton('Save', self)
        btnSave.move(90, 20)
        btnSave.clicked.connect(self.saveContent)

        self.tedtContent = QTextEdit(self)
        self.tedtContent.resize(280, 330)
        self.tedtContent.move(10, 60)

    def clearContent(self):
        currentContent = self.tedtContent.toPlainText()
        if not currentContent:
            return

        msgResponse = QMessageBox.question(self, 'New Content', 'Are you sure to clear current content',
                             QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)

        if msgResponse == QMessageBox.No:
            return

        self.tedtContent.clear()
        self.tedtContent.setFocus()

    def saveContent(self):
        options = QFileDialog.Options()
        content = self.tedtContent.toPlainText()
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File', 'xxx', 'All Files (*);;Text Files (*.txt)',
                                                  options=options)
        if filename:
            with open(filename, 'w') as f:
                f.write(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NotepadWindow()
    sys.exit(app.exec())
