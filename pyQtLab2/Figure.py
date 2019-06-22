from math import cos, sin, radians

class Figure():

    PRIMITIVE = "primitive"
    NOT_PRIMITIVE = "do not primitive"

    def __init__(self):
        self.state = self.NOT_PRIMITIVE

    def draw(self, plane):
        pass

    # def draw(self, plane, dx, dy, xc_res, yc_res, kx, ky, xc_rot, yc_rot, angle):
    #     pass

    def drawPrimitive(self, plane, qp):
        pass

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def _rotatePoint(self, x, y, xc, yc, angle):
        return xc + (x - xc) * cos(radians(angle)) + (y - yc) * sin(radians(angle)), \
               yc - (x - xc) * sin(radians(angle)) + (y - yc) * cos(radians(angle))

    def _scalePoint(self, x, y, xc, yc, kx, ky):
        return kx * x + (1 - kx) * xc, ky * y + (1 - ky) * yc

    def _movePoint(self, x, y, dx, dy):
        a = 0
        return x + dx, y + dy

