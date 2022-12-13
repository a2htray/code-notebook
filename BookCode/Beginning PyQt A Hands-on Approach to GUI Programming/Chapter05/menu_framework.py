import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction)


# QMainWindow 主要用于程序的主窗口

class BasicMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 350, 350)
        self.setWindowTitle('Basic Menu Example')

        self.createMenu()
        self.show()

    def createMenu(self):
        actExit = QAction('Exit', self)  # 设置文本及父部件
        actExit.setShortcut('Ctrl+Q')  # 设置快捷方式
        actExit.triggered.connect(self.close)  # 将窗口关闭注册到 actExit 触发事件

        menuBar = self.menuBar()  # 得到窗口的菜单条对象
        menuBar.setNativeMenuBar(False)  # 为了在 MacOS 中显示菜单条

        menuFile = menuBar.addMenu('File')  # 菜单中可以一个或多个动作 QAction
        menuFile.addAction(actExit)  # 将一个动作添加到菜单中


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicMenu()
    sys.exit(app.exec_())
