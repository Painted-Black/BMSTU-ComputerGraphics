from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import QRect, QPoint
from math import sqrt, pi, sin, cos


class MyCircle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def drawCanonEq(self, color, qp):
        qp.setPen(self._newPen(color))
        for x in range(0, self.radius + 1):
            y = round(sqrt(self.radius ** 2 - x ** 2))
            qp.drawPoint(self.center.x() + x, self.center.y() + y)
            qp.drawPoint(self.center.x() + x, self.center.y() - y)
            qp.drawPoint(self.center.x() - x, self.center.y() + y)
            qp.drawPoint(self.center.x() - x, self.center.y() - y)
        for y in range(0, self.radius + 1):
            x = round(sqrt(self.radius ** 2 - y ** 2))
            qp.drawPoint(self.center.x() + x, self.center.y() + y)
            qp.drawPoint(self.center.x() + x, self.center.y() - y)
            qp.drawPoint(self.center.x() - x, self.center.y() + y)
            qp.drawPoint(self.center.x() - x, self.center.y() - y)

    def drawParamEq(self, color, qp):
        qp.setPen(self._newPen(color))
        step = 1 / self.radius

        t = 0
        while t < 2 * pi:
            x1 = round(cos(t) * self.radius) + self.center.x()
            y1 = round(sin(t) * self.radius) + self.center.y()
            x2 = round(cos(t + step) * self.radius) + self.center.x()
            y2 = round(sin(t + step) * self.radius) + self.center.y()
            qp.drawLine(x1, y1, x2, y2)
            t += step

        # qp.setPen(self._newPen(color))
        # l = round(pi * self.radius / 2)  # длина четврети окружности
        # for i in range(0, l + 1, 1):
        #     x = round(self.radius * cos(i / self.radius))
        #     y = round(self.radius * sin(i / self.radius))
        #     qp.drawPoint(self.center.x() + x, self.center.y() + y)
        #     qp.drawPoint(self.center.x() + x, self.center.y() - y)
        #     qp.drawPoint(self.center.x() - x, self.center.y() + y)
        #     qp.drawPoint(self.center.x() - x, self.center.y() - y)

    def drawBresenhamAlgorithm(self, color, qp):
        qp.setPen(self._newPen(color))
        x = 0
        y = self.radius
        d = 2 * (1 - self.radius)
        while y >= 0:
            qp.drawPoint(self.center.x() + x, self.center.y() + y)
            qp.drawPoint(self.center.x() + x, self.center.y() - y)
            qp.drawPoint(self.center.x() - x, self.center.y() + y)
            qp.drawPoint(self.center.x() - x, self.center.y() - y)
            if d < 0:
                d1 = 2 * d + 2 * y - 1
                x += 1
                if d1 <= 0:
                    d = d + 2 * x + 1
                elif d1 > 0:
                    y -= 1
                    d += 2 * (x - y + 1)
            elif d > 0:
                d2 = 2 * d - 2 * x - 1
                y -= 1
                if d2 <= 0:
                    x += 1
                    d += 2 * (x - y + 1)
                else:
                    d = d - 2 * y + 1
            else:
                x += 1
                y -= 1
                d += 2 * (x - y + 1)

    def drawMiddleDotAlgorithm(self, color, qp):
        qp.setPen(self._newPen(color))
        x = 0
        y = self.radius
        p = 5 / 4 - self.radius
        while x <= y:
            qp.drawPoint(self.center.x() + x, self.center.y() + y)
            qp.drawPoint(self.center.x() + x, self.center.y() - y)
            qp.drawPoint(self.center.x() - x, self.center.y() + y)
            qp.drawPoint(self.center.x() - x, self.center.y() - y)

            qp.drawPoint(self.center.x() + y, self.center.y() + x)
            qp.drawPoint(self.center.x() + y, self.center.y() - x)
            qp.drawPoint(self.center.x() - y, self.center.y() + x)
            qp.drawPoint(self.center.x() - y, self.center.y() - x)

            x += 1

            if p < 0:
                p += 2 * x + 1
            else:
                p += 2 * x - 2 * y + 5
                y -= 1

    def drawLibraryAlgorithm(self, color, qp):
        newPen = self._newPen(color)
        qp.setPen(newPen)
        qp.drawEllipse(self.center, self.radius, self.radius)

    def _newPen(self, color):
        newPen = QPen()
        newColor = QColor(color)
        newPen.setColor(newColor)
        return newPen
