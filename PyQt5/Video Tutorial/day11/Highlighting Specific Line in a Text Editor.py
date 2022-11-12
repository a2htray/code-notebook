# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QVBoxLayout, QLineEdit, QBoxLayout, QPushButton
from PyQt5.QtCore import QRegExp, pyqtSignal
from PyQt5.QtGui import QColor, QRegExpValidator, QSyntaxHighlighter, QTextCharFormat, QFont


class HighlightNumberInput(QWidget):
    """Highlight number input"""

    highlightClicked = pyqtSignal(int)

    def __init__(self, parent):
        super().__init__(parent)

        layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.lineEdit = QLineEdit(self)
        self.stylizeLineEdit()

        # 输入框正则
        validator = QRegExpValidator(QRegExp(r'[0-9]*'))
        self.lineEdit.setValidator(validator)

        self.pushButton = QPushButton('Highlight', self)
        self.stylizePushButton()
        self.pushButton.clicked.connect(self.onClick)

        layout.addWidget(self.lineEdit)
        layout.addWidget(self.pushButton)

        self.setLayout(layout)

    def stylizeLineEdit(self):
        self.lineEdit.setStyleSheet('font-size: 25px; color: green;')

    def stylizePushButton(self):
        self.pushButton.setStyleSheet('font-size: 25px; font-style: italic;')

    def onClick(self):
        print('HighlightNumberInput.onClick')
        try:
            print(int(self.lineEdit.text()))
            lineNumber = int(self.lineEdit.text()) - 1
            self.highlightClicked.emit(lineNumber)
        except Exception as exception:
            print(exception)


class SyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super().__init__(parent)
        self._highlightLines = {}

    def highlightLine(self, lineNumber, format):
        if isinstance(lineNumber, int) and lineNumber > 0 and isinstance(format, QTextCharFormat):
            self._highlightLines[lineNumber] = format
            block = self.document().findBlockByLineNumber(lineNumber)
            self.rehighlightBlock(block)

    def clearHighlight(self):
        self._highlightLines = {}
        self.rehighlight()

    def highlightBlock(self, text: str) -> None:
        blockNumber = self.currentBlock().blockNumber()
        format = self._highlightLines.get(blockNumber)
        if format is not None:
            self.setFormat(0, len(text), format)


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        layout = QVBoxLayout()

        self.highlightNumberInput = HighlightNumberInput(parent=self)
        self.highlightNumberInput.highlightClicked.connect(self.onHighlightClick)
        self.plainTextEdit = QPlainTextEdit(parent=self)
        self.stylize()

        for i in range(0, 100):
            self.plainTextEdit.appendPlainText(f'test line {i+1}')

        self.highlighter = SyntaxHighlighter(self.plainTextEdit.document())

        layout.addWidget(self.highlightNumberInput)
        layout.addWidget(self.plainTextEdit)

        self.setLayout(layout)

    def onHighlightClick(self, lineNumer):
        format = QTextCharFormat()
        format.setBackground(QColor('yellow'))

        self.highlighter.clearHighlight()
        self.highlighter.highlightLine(lineNumer, format)

    def stylize(self):
        self.plainTextEdit.setStyleSheet('font-size: 20px; color: #DBDBDA; font-style: italic;')


if __name__ == '__main__':
    app = QApplication([])

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())
