from PyQt5.QtGui import QPainter, QPainterPath
from PyQt5.QtCore import QPoint
from Include.Figure import *
from math import pi, cos, sin, radians

class MyCircle(Figure):
    
    def __init__(self, xrad, yrad, xc, yc):
        super().__init__()
        self.x_height = xrad
        self.y_height = yrad
        self.center_x = xc
        self.center_y = yc
        self.rot_cx = 0
        self.rot_cy = 0
        self.angle = 0

    def incAngle(self, a):
        self.angle += a
        self.angle %= 360

    def draw(self, plane):
        path = QPainterPath()

        for i in range(360):
            x = cos(radians(i)) * self.x_height + self.center_x
            y = sin(radians(i)) * self.y_height + self.center_y
            x, y = self._rotatePoint(x, y, self.center_x, self.center_y, self.angle)
            if i == 0:
                path.moveTo(x, y)
            else:
                path.lineTo(x, y)
        return path

    def rotate(self, xc, yc, angle):
        self.center_x, self.center_y = self._rotatePoint(self.center_x, self.center_y, xc, yc, angle)
        self.rot_cx, self.rot_cy = xc, yc
        self.incAngle(angle)

    def move(self, dx, dy):
        self.center_x += dx
        self.center_y += dy

    def scale(self, kx, ky, xc, yc):
        self.center_x, self.center_y = self._scalePoint(self.center_x, self.center_y,
                                                        xc, yc, kx, ky)
        self.x_height *= kx
        self.y_height *= ky

    def scale1(self, rx, ry, xc, yc, kx, ky):
        # self.center_x, self.center_y = self._scalePoint(self.center_x, self.center_y,
        #                                                 xc, yc, kx, ky)
        self.center_x, self.center_y = xc, yc
        self.x_height = rx
        self.y_height = ry



    # def drawPrimitive(self, plane, qp, dx, dy, xc_res, yc_res, kx, ky, xc_rot, yc_rot, angle):
    #     oneUnit = plane.oneUnit()
    #     print(oneUnit)
    #     x = plane.centerPoint()[0]
    #     y = plane.centerPoint()[1]
    #     x, y = self._scalePoint(x, y, xc_res, yc_res, kx, ky)
    #     x, y = self._movePoint(x, y, dx, dy)
    #     x, y = self._rotatePoint(x, y, xc_rot, yc_rot, angle)
    #     # x *= oneUnit
    #     # y *= oneUnit
    #     # x, y = self._rotatePoint(x, y, xc_rot + plane.centerPoint()[0],
    #     #                          yc_rot - plane.centerPoint()[1], angle)
    #     print(x, y)
    #     x_rad = self.x_height * kx * oneUnit / 2
    #     y_rad = self.y_height * ky * oneUnit / 2
    #     point = QPoint(x, y)
    #     qp.drawEllipse(point, x_rad * 2, y_rad * 2)
