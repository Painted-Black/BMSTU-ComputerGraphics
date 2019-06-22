from DrawableObject import *
from Algorithm import *

from math import sin, cos, radians
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QRect, QPoint


class SegmentSpectrum(DrawableObject):

    def __init__(self, len, step, drawCenter, alg=Algorithm.DDA, color=QColor().black(), x=0, y=0):
        self.length = len
        self.step = step
        self.algorithm = alg
        self.color = color
        self.drawCenter = drawCenter
        self.xs = x
        self.ys = y

    def draw(self, sizeScreen, qp):
        if self.drawCenter:
            self.xs = sizeScreen[0] / 2
            self.ys = sizeScreen[1] / 2

        angle = 0
        while angle <= 360:
            xe = round(self.xs + cos(radians(angle)) * self.length)
            ye = round(self.ys - sin(radians(angle)) * self.length)
            self.drawLine(qp, xe, ye)
            angle += self.step

    def drawLine(self, qp, xe, ye):
        if self.algorithm == Algorithm.DDA:
            x, y = DrawableObject._drawDDA(self, self.xs, self.ys, xe, ye, self.color, qp)
            if x != None and y != None:
                qp.setPen(DrawableObject._newPen(self, QColor(Qt.red)))
                qp.drawEllipse(QPoint(x, y), 10, 10)
        elif self.algorithm == Algorithm.BRN:
            x, y = DrawableObject._drawBRN(self, self.xs, self.ys, xe, ye, self.color, qp)
            if x != None and y != None:
                qp.setPen(DrawableObject._newPen(self, QColor(Qt.red)))
                qp.drawEllipse(QPoint(x, y), 10, 10)
        elif self.algorithm == Algorithm.BIN:
            x, y = DrawableObject._drawBIN(self, self.xs, self.ys, xe, ye, self.color, qp)
            if x != None and y != None:
                qp.setPen(DrawableObject._newPen(self, QColor(Qt.red)))
                qp.drawEllipse(QPoint(x, y), 10, 10)
        elif self.algorithm == Algorithm.BAA:
            x, y = DrawableObject._drawBAA(self, self.xs, self.ys, xe, ye, self.color, qp)
            if x != None and y != None:
                qp.setPen(DrawableObject._newPen(self, QColor(Qt.red)))
                qp.drawEllipse(QPoint(x, y), 10, 10)
        elif self.algorithm == Algorithm.LA:
            DrawableObject._drawLA(self, self.xs, self.ys, xe, ye, self.color, qp)
