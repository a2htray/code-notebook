# -*- coding=utf-8 -*-
r"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsEllipseItem, QGraphicsScene, \
    QGraphicsSceneHoverEvent, QGraphicsSceneMouseEvent
from PyQt5.QtCore import Qt, QPointF


class MovingObject(QGraphicsEllipseItem):
    def __init__(self, x, y, r):
        super().__init__(0, 0, r, r)
        self.setPos(x, y)
        self.setBrush(Qt.blue)

        self.setAcceptHoverEvents(True)

    def hoverEnterEvent(self, event: QGraphicsSceneHoverEvent) -> None:
        print('hoverEnterEvent')
        QApplication.setOverrideCursor(Qt.OpenHandCursor)

    def hoverLeaveEvent(self, event: QGraphicsSceneHoverEvent) -> None:
        print('hoverLeaveEvent')
        QApplication.restoreOverrideCursor()

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        print('mousePressEvent')

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        cursorLastPos = event.lastScenePos()
        cursorCurrentPos = event.scenePos()

        pos = self.scenePos()

        self.setPos(QPointF(
            cursorCurrentPos.x() - cursorLastPos.x() + pos.x(),
            cursorCurrentPos.y() - cursorLastPos.y() + pos.y(),
        ))

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        print('mouseReleaseEvent')


class GraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setSceneRect(0, 0, 1200, 1000)

        self.movingObject = MovingObject(50, 50, 40)
        self.scene.addItem(self.movingObject)


if __name__ == '__main__':
    app = QApplication([])

    view = GraphicsView()
    view.show()

    sys.exit(app.exec())
