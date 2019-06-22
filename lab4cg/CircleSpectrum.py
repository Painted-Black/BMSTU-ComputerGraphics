from DrawableObjet import *
from Algorithm import *
from MyCircle import *


class CircleSpectrum(DrawableObject):

    def __init__(self, center, startRadius, count, step, alg, color):
        self.center = center
        self.startRadius = startRadius
        self.count = count
        self.step = step
        self.algorithm = alg
        self.color = color

    def draw(self, sizeScreen, qp):
        curRad = self.startRadius
        for i in range(0, self.count):
            circle = MyCircle(self.center, curRad)
            if self.algorithm == Algorithm.CANON_EQ:
                circle.drawCanonEq(self.color, qp)
            elif self.algorithm == Algorithm.PARA_EQ:
                circle.drawParamEq(self.color, qp)
            elif self.algorithm == Algorithm.BRESENHAM_ALG:
                circle.drawBresenhamAlgorithm(self.color, qp)
            elif self.algorithm == Algorithm.MIDDLE_DOT_ALG:
                circle.drawMiddleDotAlgorithm(self.color, qp)
            elif self.algorithm == Algorithm.LIBRARY_ARG:
                circle.drawLibraryAlgorithm(self.color, qp)
            curRad += self.step


