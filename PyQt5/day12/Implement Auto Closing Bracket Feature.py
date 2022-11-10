# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QTextEdit
from PyQt5.QtGui import QFont, QKeyEvent


class TextEdit(QTextEdit):
    def __init__(self):
        super().__init__()

        self.setFont(QFont('Open sans', 20))

    def keyPressEvent(self, event: QKeyEvent) -> None:
        characterList = {
            '[': ']',
            '(': ')',
            "'": "'",
            '"': ':',
            '{': '}',
        }

        closindCharacter = characterList.get(event.text())
        if closindCharacter:
            cursor = self.textCursor()
            position = cursor.position()
            print(f'cursor position: {position}')
            self.insertPlainText(closindCharacter)

            cursor.setPosition(position)
            self.setTextCursor(cursor)

        super().keyPressEvent(event)


if __name__ == '__main__':
    app = QApplication([])

    demo = TextEdit()
    demo.show()

    sys.exit(app.exec())
