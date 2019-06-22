from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import QRect, QPoint
from math import sqrt, pi, sin, cos


class MyEllipse:
    def __init__(self, center, axisX, axisY):
        self.center = center
        self.axisX = axisX
        self.axisY = axisY

    def drawCanonEq(self, color, qp):
        qp.setPen(self._newPen(color))
        for x in range(0, self.axisX + 1):
            y = round(self.axisY * sqrt(1 - x ** 2 / self.axisX ** 2))
            qp.drawPoint(self.center.x() + x, self.center.y() + y)
            qp.drawPoint(self.center.x() + x, self.center.y() - y)
            qp.drawPoint(self.center.x() - x, self.center.y() + y)
            qp.drawPoint(self.center.x() - x, self.center.y() - y)
        for y in range(0, self.axisY + 1):
            x = round(self.axisX * sqrt(1 - y ** 2 / self.axisY ** 2))
            qp.drawPoint(self.center.x() + x, self.center.y() + y)
            qp.drawPoint(self.center.x() + x, self.center.y() - y)
            qp.drawPoint(self.center.x() - x, self.center.y() + y)
            qp.drawPoint(self.center.x() - x, self.center.y() - y)

    def drawParamEq(self, color, qp):
        qp.setPen(self._newPen(color))
        step = 1 / max(self.axisX, self.axisY)
        t = step
        while t < pi / 2:
            x1 = self.center.x() + self.axisX * cos(t)
            y1 = self.center.y() + self.axisY * sin(t)
            x2 = self.center.x() + self.axisX * cos(t + step)
            y2 = self.center.y() + self.axisY * sin(t + step)

            x3 = self.center.x() + self.axisX * cos(t)
            y3 = self.center.y() - self.axisY * sin(t)
            x4 = self.center.x() + self.axisX * cos(t + step)
            y4 = self.center.y() - self.axisY * sin(t + step)

            x5 = self.center.x() - self.axisX * cos(t)
            y5 = self.center.y() + self.axisY * sin(t)
            x6 = self.center.x() - self.axisX * cos(t + step)
            y6 = self.center.y() + self.axisY * sin(t + step)

            x7 = self.center.x() - self.axisX * cos(t)
            y7 = self.center.y() - self.axisY * sin(t)
            x8 = self.center.x() - self.axisX * cos(t + step)
            y8 = self.center.y() - self.axisY * sin(t + step)

            qp.drawLine(x1, y1, x2, y2)
            qp.drawLine(x3, y3, x4, y4)
            qp.drawLine(x5, y5, x6, y6)
            qp.drawLine(x7, y7, x8, y8)

            t += step

        # m = max(self.axisX, self.axisY)
        # l = round(pi * m / 2)
        # for i in range(0, l + 1, 1):
        #     x = round(self.axisX * cos(i / m))
        #     y = round(self.axisY * sin(i / m))
        #     qp.drawPoint(self.center.x() + x, self.center.y() + y)
        #     qp.drawPoint(self.center.x() + x, self.center.y() - y)
        #     qp.drawPoint(self.center.x() - x, self.center.y() + y)
        #     qp.drawPoint(self.center.x() - x, self.center.y() - y)

    def drawBresenhamAlgorithm(self, color, qp):
        qp.setPen(self._newPen(color))
        x = 0
        y = self.axisY
        a = self.axisX ** 2
        d = round(self.axisY ** 2 / 2 - self.axisX * self.axisY * 2 + self.axisX / 2)
        b = self.axisY ** 2
        while y >= 0:
            qp.drawPoint(self.center.x() + x, self.center.y() + y)
            qp.drawPoint(self.center.x() + x, self.center.y() - y)
            qp.drawPoint(self.center.x() - x, self.center.y() + y)
            qp.drawPoint(self.center.x() - x, self.center.y() - y)

            if d < 0:
                d1 = 2 * d + 2 * a * y - a
                x += 1
                if d1 <= 0:
                    d = d + 2 * b * x + b
                else:
                    y -= 1
                    d = d + 2 * b * x - 2 * a * y + a + b
            elif d > 0:
                d2 = 2 * d - 2 * b * x - b
                y -= 1
                if d2 > 0:
                    d = d - 2 * y * a + a
                else:
                    x += 1
                    d = d + 2 * x * b - 2 * y * a + a + b
            else:
                x += 1
                y -= 1
                d = d + 2 * x * b - 2 * y * a + a + b

    def drawMiddleDotAlgorithm(self, color, qp):
        qp.setPen(self._newPen(color))
        x = 0
        y = self.axisY
        p = self.axisY ** 2 - self.axisX ** 2 * self.axisY + 0.25 * self.axisX ** 2
        a = self.axisX
        b = self.axisY

        while 2 * (b ** 2) * x < 2 * (a ** 2) * y:
            qp.drawPoint(self.center.x() + x, self.center.y() + y)
            qp.drawPoint(self.center.x() + x, self.center.y() - y)
            qp.drawPoint(self.center.x() - x, self.center.y() + y)
            qp.drawPoint(self.center.x() - x, self.center.y() - y)

            x += 1
            if p < 0:
                p += 2 * b * b * x + b * b
            else:
                y -= 1
                p += 2 * b * b * x - 2 * a * a * y + b * b

        p = b * b * (x + 0.5) * (x + 0.5) + a * a * (y - 1) * (y - 1) - a * a * b * b

        while y >= 0:
            qp.drawPoint(self.center.x() + x, self.center.y() + y)
            qp.drawPoint(self.center.x() + x, self.center.y() - y)
            qp.drawPoint(self.center.x() - x, self.center.y() + y)
            qp.drawPoint(self.center.x() - x, self.center.y() - y)
            y -= 1

            if p > 0:
                p -= 2 * a * a * y + a * a
            else:
                x += 1
                p += 2 * b * b * x - 2 * a * a * y + a * a

    def drawLibraryAlgorithm(self, color, qp):
        newPen = self._newPen(color)
        qp.setPen(newPen)
        qp.drawEllipse(self.center, self.axisX, self.axisY)

    def _newPen(self, color):
        newPen = QPen()
        newColor = QColor(color)
        newPen.setColor(newColor)
        return newPen
