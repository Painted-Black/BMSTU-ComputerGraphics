from DrawableObject import *
from PyQt5.QtGui import QColor
from Algorithm import *


class Segment(DrawableObject):

    def __init__(self, xs, ys, xe, ye, alg, color=QColor().black()):
        self.xs = xs
        self.ys = ys
        self.xe = xe
        self.ye = ye
        self.color = color
        self.algorithm = alg

    def draw(self, sizeScreen, qp):
        if self.algorithm == Algorithm.DDA:
            DrawableObject._drawDDA(self, self.xs, self.ys, self.xe, self.ye, self.color, qp)
        elif self.algorithm == Algorithm.BRN:
            DrawableObject._drawBRN(self, self.xs, self.ys, self.xe, self.ye, self.color, qp)
        elif self.algorithm == Algorithm.BIN:
            DrawableObject._drawBIN(self, self.xs, self.ys, self.xe, self.ye, self.color, qp)
        elif self.algorithm == Algorithm.BAA:
            DrawableObject._drawBAA(self, self.xs, self.ys, self.xe, self.ye, self.color, qp)
        elif self.algorithm == Algorithm.LA:
            DrawableObject._drawLA(self, self.xs, self.ys, self.xe, self.ye, self.color, qp)
