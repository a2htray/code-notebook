# -*- coding=utf-8 -*-
r"""
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QAction, QFileDialog, QDesktopWidget, \
    QMessageBox, QSizePolicy, QToolBar, QStatusBar, QDockWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QTransform, QPainter
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog


class Action(QAction):
    def __init__(self, parent, iconUrl='', text='', shortcut='', statusTip='', triggeredSlot=''):
        if iconUrl:
            super().__init__(QIcon(iconUrl), text, parent)
        else:
            super().__init__(text, parent)

        if shortcut:
            self.setShortcut(shortcut)

        if statusTip:
            self.setStatusTip(statusTip)

        self.triggered.connect(triggeredSlot)


class PhotoEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setFixedSize(650, 650)
        self.setWindowTitle('Photo Editor GUI')

        # self.centerMainWindow()
        self.createToolsDockWidget()
        self.createMenu()
        # self.createToolBar()
        self.photoEditorWidgets()
        self.show()

    def createMenu(self):
        self.open_act = Action(self, 'assets/open_file.png', 'Open', 'Ctrl+O', 'Open a new image', self.openImage)
        self.save_act = Action(self, 'assets/save_file.png', 'Save', 'Ctrl+S', 'Save image', self.saveImage)
        self.print_act = Action(self, 'assets/print.png', 'Print', 'Ctrl+P', 'Print image', self.printImage)
        self.print_act.setEnabled(False)
        self.exit_act = Action(self, 'assets/exit.png', 'Exit', 'Ctrl+Q', 'Quit program', self.close)

        self.rotate90_act = Action(self, text='Rotate 90', statusTip='Rotate image 90° clockwise',
                                   triggeredSlot=self.rotateImage90)
        self.rotate180_act = Action(self, text='Rotate 180', statusTip='Rotate image 180° clockwise',
                                   triggeredSlot=self.rotateImage180)
        self.flip_hor_act = Action(self, text='Flip Horizontal', statusTip='Flip image across horizontal axis',
                                   triggeredSlot=self.flipImageHorizontal)
        self.flip_ver_act = Action(self, text='Flip Vertical', statusTip='Flip image across vertical axis',
                                   triggeredSlot=self.flipImageVertical)
        self.resize_act = Action(self, text='Resize Half', statusTip='Resize image to half the original size',
                                   triggeredSlot=self.resizeImageHalf)
        self.clear_act = Action(self, 'assets/clear_file.png', 'Clear Image', 'Ctrl+D', 'Clear the current image',
                                self.clearImage)

        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(self.open_act)
        file_menu.addAction(self.save_act)
        file_menu.addSeparator()
        file_menu.addAction(self.print_act)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_act)

        edit_menu = menu_bar.addMenu('Edit')
        edit_menu.addAction(self.rotate90_act)
        edit_menu.addAction(self.rotate180_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.flip_hor_act)
        edit_menu.addAction(self.flip_ver_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.resize_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.clear_act)

        view_menu = menu_bar.addMenu('View')
        view_menu.addAction(self.toggle_dock_tools_act)

        self.setStatusBar(QStatusBar(self))

    def createToolsDockWidget(self):
        self.dock_tools_view = QDockWidget()
        self.dock_tools_view.setWindowTitle('Edit Image Tools')
        self.dock_tools_view.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

        self.tools_contents = QWidget()

        self.rotate90 = QPushButton('Rotate 90°')
        self.rotate90.setMinimumSize(QSize(130, 40))
        self.rotate90.setStatusTip('Rotate image 90° clockwise')
        self.rotate90.clicked.connect(self.rotateImage90)

        self.rotate180 = QPushButton("Rotate 180°")
        self.rotate180.setMinimumSize(QSize(130, 40))
        self.rotate180.setStatusTip('Rotate image 180° clockwise')
        self.rotate180.clicked.connect(self.rotateImage180)

        self.flip_horizontal = QPushButton("Flip Horizontal")
        self.flip_horizontal.setMinimumSize(QSize(130, 40))
        self.flip_horizontal.setStatusTip('Flip image across horizontal axis')
        self.flip_horizontal.clicked.connect(self.flipImageHorizontal)

        self.flip_vertical = QPushButton("Flip Vertical")
        self.flip_vertical.setMinimumSize(QSize(130, 40))
        self.flip_vertical.setStatusTip('Flip image across vertical axis')
        self.flip_vertical.clicked.connect(self.flipImageVertical)
        self.resize_half = QPushButton("Resize Half")
        self.resize_half.setMinimumSize(QSize(130, 40))
        self.resize_half.setStatusTip('Resize image to half the original size')
        self.resize_half.clicked.connect(self.resizeImageHalf)
        # Set up vertical layout to contain all the push buttons
        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(self.rotate90)
        dock_v_box.addWidget(self.rotate180)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.flip_horizontal)
        dock_v_box.addWidget(self.flip_vertical)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.resize_half)
        dock_v_box.addStretch(6)
        # Set the main layout for the QWidget, tools_contents,
        # then set the main widget of the dock widget
        self.tools_contents.setLayout(dock_v_box)
        self.dock_tools_view.setWidget(self.tools_contents)
        # Set initial location of dock widget
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_tools_view)
        # Handles the visibility of the dock widget
        self.toggle_dock_tools_act = self.dock_tools_view.toggleViewAction()

    def photoEditorWidgets(self):
        self.image = QPixmap()
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        # Use setSizePolicy to specify how the widget can be resized,
        # horizontally and vertically. Here, the image will stretch
        # horizontally, but not vertically.
        self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        self.setCentralWidget(self.image_label)

    def openImage(self):
        image_file, _ = QFileDialog.getOpenFileName(
            self,
            'Open Image',
            '',
            'JPG Files (*.jpeg *.jpg );;PNG Files (*.png);;Bitmap Files (*.bmp);;GIF Files (*.gif)',
        )
        if image_file:
            self.image = QPixmap(image_file)
            self.image_label.setPixmap(
                self.image.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            QMessageBox.information(self,
                                    'Error',
                                    'Unable to open image.',
                                    QMessageBox.Ok)
        self.print_act.setEnabled(True)

    def saveImage(self):
        image_file, _ = QFileDialog.getSaveFileName(
            self,
            'Save Image',
            '',
            'JPG Files (*.jpeg *.jpg );;PNG Files (*.png);;Bitmap Files(*.bmp);;GIF Files (*.gif)',
        )
        if image_file and not self.image.isNull():
            self.image.save(image_file)
        else:
            QMessageBox.information(
                self,
                'Error',
                'Unable to save image.',
                QMessageBox.Ok,
            )

    def printImage(self):
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.NativeFormat)
        # Create printer dialog to configure printer
        print_dialog = QPrintDialog(printer)
        # If the dialog is accepted by the user, begin printing
        if print_dialog.exec_() == QPrintDialog.Accepted:
            # Use QPainter to output a PDF file
            painter = QPainter()
            # Begin painting device
            painter.begin(printer)
            # Set QRect to hold painter's current viewport, which
            # is the image_label
            rect = QRect(painter.viewport())
            # Get the size of image_label and use it to set the size
            # of the viewport
            size = QSize(self.image_label.pixmap().size())
            size.scale(rect.size(), Qt.KeepAspectRatio)

            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image_label.pixmap().rect())
            # Scale the image_label to fit the rect source (0, 0)
            painter.drawPixmap(0, 0, self.image_label.pixmap())
            # End painting
            painter.end()

    def rotateImage90(self):
        if not self.image.isNull():
            transform90 = QTransform().rotate(90)
            pixmap = QPixmap(self.image)
            rotated = pixmap.transformed(transform90, mode=Qt.SmoothTransformation)
            self.image_label.setPixmap(rotated.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image = QPixmap(rotated)
            self.image_label.repaint()

    def rotateImage180(self):
        pass

    def flipImageHorizontal(self):
        pass

    def flipImageVertical(self):
        pass

    def resizeImageHalf(self):
        pass

    def clearImage(self):
        self.image_label.clear()
        self.image = QPixmap()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PhotoEditor()
    sys.exit(app.exec())


