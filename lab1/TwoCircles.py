import sympy
from TangentPosition import *
from PyQt5.QtGui import QPen, QPainter
from PyQt5.QtCore import QPoint
from Point import *

class TwoCircles:
    def __init__(self, c1, c2, r1, r2, tangent_pos):
        self.c1 = c1
        self.c2 = c2
        self.rad1 = r1
        self.rad2 = r2
        self.tangentPosition = tangent_pos
        a = 4

    def draw(self, qp, kx, ky, dx, dy, sizeScreen):
        # qp = QPainter()

        qp.drawEllipse(QPoint((self.c1.get_x() + dx) * kx, sizeScreen[1] - (self.c1.get_y() + dy) * ky),
                       self.rad1 * kx, self.rad1 * ky)
        qp.drawEllipse(QPoint((self.c2.get_x() + dx) * kx, sizeScreen[1] - (self.c2.get_y() + dy) * kx),
                       self.rad2 * kx, self.rad2 * ky)

        point1 = QPoint(round((self.tangentPosition[1].get_x() + dx) * kx),
                        round(sizeScreen[1] - (self.tangentPosition[1].get_y() + dy) * ky))
        point2 = QPoint(round((self.tangentPosition[0].get_x() + dx) * kx),
                        round(sizeScreen[1] - (self.tangentPosition[0].get_y() + dy) * ky))

        # print(point1)
        # print(point2)

        # point1 = MyPoint(point1.get_x(), point1.get_y())
        # point2 = MyPoint(point2.get_x(), point2.get_y())
        if point1.x() < point2.x():
            point1 = QPoint(point1.x() - 100, point1.y())
            point2 = QPoint(point2.x() + 100, point2.y())
        else:
            point1 = QPoint(point1.x() + 100, point1.y())
            point2 = QPoint(point2.x() - 100, point2.y())
        # print(point1)
        # print(point2)

        qp.drawLine(point1, point2)
        # print(self.tangentPosition

    def getCircles(self):
        return self.c1, self.c2, self.rad1, self.rad2
