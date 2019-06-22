from DrawableObjet import *
from MyEllipse import *
from Algorithm import *


class EllipseSpectrum(DrawableObject):

    def __init__(self, center, axisX, axisY, count, stepX, stepY, alg, color):
        self.center = center
        self.axisX = axisX
        self.axisY = axisY
        self.count = count
        self.stepX = stepX
        self.stepY = stepY
        self.algorithm = alg
        self.color = color

    def draw(self, sizeScreen, qp):
        curAxisX = self.axisX
        curAxisY = self.axisY
        for i in range(0, self.count):
            ellipse = MyEllipse(self.center, curAxisX, curAxisY)
            if self.algorithm == Algorithm.CANON_EQ:
                ellipse.drawCanonEq(self.color, qp)
            elif self.algorithm == Algorithm.PARA_EQ:
                ellipse.drawParamEq(self.color, qp)
            elif self.algorithm == Algorithm.BRESENHAM_ALG:
                ellipse.drawBresenhamAlgorithm(self.color, qp)
            elif self.algorithm == Algorithm.MIDDLE_DOT_ALG:
                ellipse.drawMiddleDotAlgorithm(self.color, qp)
            elif self.algorithm == Algorithm.LIBRARY_ARG:
                ellipse.drawLibraryAlgorithm(self.color, qp)
            curAxisX += self.stepX
            curAxisY += self.stepY
