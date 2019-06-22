from PyQt5.QtGui import QPainterPath
from Include.Figure import *
import math

class Rect(Figure):
    def __init__(self, xc, yc, height, width):
        super().__init__()
        self.xc = xc
        self.yc = yc
        self.height = height
        self.width = width
        self.rot_xc = 0
        self.rot_yc = 0
        self.angle = 0

    def draw(self, plane):
        qp = QPainterPath()

        x = self.xc + self.width / 2
        y = self.yc
        x, y = self._rotatePoint(x, y, self.xc, self.yc, self.angle)
        qp.moveTo(x, y)

        x = self.xc + self.width / 2
        y = self.yc + self.height
        x, y = self._rotatePoint(x, y, self.xc, self.yc, self.angle)
        qp.lineTo(x, y)

        x = self.xc - self.width / 2
        y = self.yc + self.height
        x, y = self._rotatePoint(x, y, self.xc, self.yc, self.angle)
        qp.lineTo(x, y)

        x = self.xc - self.width / 2
        y = self.yc
        x, y = self._rotatePoint(x, y, self.xc, self.yc, self.angle)
        qp.lineTo(x, y)

        qp.lineTo(x, y)
        return qp

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
            return 4 * math.cos(t) ** 3