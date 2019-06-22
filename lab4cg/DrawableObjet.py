from abc import ABC, abstractmethod

from PyQt5.QtGui import QPen, QColor


class DrawableObject(ABC):

    @abstractmethod
    def draw(self, sizeScreen, qp):
        pass

    def _newPen(self, color):
        newPen = QPen()
        newColor = QColor(color)
        newPen.setColor(newColor)
        return newPen
