from PyQt5.QtGui import QPainterPath
from PyQt5.QtCore import QPoint
from Include.Figure import *
import math

class Astroid(Figure):
    def __init__(self, xc, yc, height, width):
        super().__init__()
        self.xc = xc
        self.yc = yc
        self.height = height
        self.width = width
        self.rot_xc = 0
        self.rot_yc = 0
        self.angle = 0

    def draw(self, coord):
        path = QPainterPath()
        # path = QPainterPath(QPoint((self.width / 4) + self.xc, (self.height / 4) + self.yc))
        i = 0

        x = self.__x(i) * (self.width / 4) + self.xc
        y = self.__y(i) * (self.height / 4) + self.yc
        x, y = self._rotatePoint(x, y, self.xc, self.yc, self.angle)
        path.moveTo(x, y)
        while i < 2*math.pi:
            path.lineTo(x, y)
            x = self.__x(i) * (self.width / 4) + self.xc
            y = self.__y(i) * (self.height / 4) + self.yc
            x, y = self._rotatePoint(x, y, self.xc, self.yc, self.angle)
            i += 0.1

        return path

    def move(self, dx, dy):
        self.xc += dx
        self.yc += dy

    def scale(self, kx, ky, xc, yc):
        self.xc, self.yc = self._scalePoint(self.xc, self.yc,
                                                        xc, yc, kx, ky)
        self.height *= ky
        self.width *= kx

    def scale1(self, rx, ry, xc, yc, kx, ky):
        # self.xc, self.yc = self._scalePoint(self.xc, self.yc,
        #                                                 xc, yc, kx, ky)
        self.xc, self.yc = xc, yc
        self.height = rx
        self.width = ry

    def rotate(self, xc, yc, angle):
        self.xc, self.yc = self._rotatePoint(self.xc, self.yc, xc, yc, angle)
        self.rot_cx, self.rot_cy = xc, yc
        self.incAngle(angle)

    def incAngle(self, a):
        self.angle += a
        self.angle %= 360

    def __x(self, t):
        return 4 * math.cos(t)**3

    def __y(self, t):
        return 4 * math.sin(t)**3
