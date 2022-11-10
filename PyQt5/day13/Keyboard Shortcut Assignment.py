# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QShortcut, QLabel, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence


class Demo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.labelDisplay = QLabel(self)
        self.labelDisplay.setStyleSheet('font-size: 60px;')
        self.setCentralWidget(self.labelDisplay)
        self.labelDisplay.setAlignment(Qt.AlignCenter)

        self.shortcut = QShortcut(QKeySequence('Ctrl+O'), self)
        self.shortcut.activated.connect(
            lambda shortcutKey=self.shortcut.key().toString(): self.displayKeys(shortcutKey)
        )

        self.shortcut = QShortcut(QKeySequence.Undo, self)
        self.shortcut.activated.connect(
            lambda shortcutKey=self.shortcut.key().toString(): self.displayKeys(shortcutKey)
        )

        self.shortcut = QShortcut(QKeySequence('Ctrl+Shift+T'), self)
        self.shortcut.activated.connect(
            lambda shortcutKey=self.shortcut.key().toString(): self.displayKeys(shortcutKey)
        )

        self.shortcut = QShortcut(QKeySequence('Ctrl+Shift+Space'), self)
        self.shortcut.activated.connect(
            lambda shortcutKey=self.shortcut.key().toString(): self.displayKeys(shortcutKey)
        )

    def displayKeys(self, mapping):
        # print(mapping)
        self.labelDisplay.setText(mapping)
        self.labelDisplay.show()


if __name__ == '__main__':
    app = QApplication([])

    demo = Demo()
    demo.show()

    sys.exit(app.exec())
