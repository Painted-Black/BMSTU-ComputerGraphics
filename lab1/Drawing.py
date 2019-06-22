from PyQt5.QtWidgets import QWidget, QGridLayout, QDesktopWidget
from CoordinatePlane import *
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPen, QStaticText
import random
from Point import *


class Drawing(QWidget):
    def __init__(self, figures, set1, set2):
        super().__init__()

        self.pannel = QWidget(self)
        self.layout = QGridLayout()
        self.qp = QPainter()
        self.sizeScreen = [QDesktopWidget().availableGeometry().width() - 100,
                           QDesktopWidget().availableGeometry().height() - 100]
        self.coordinatePlane = None
        self.kx = 1
        self.ky = 1
        self.dx = 0
        self.dy = 0

        self.figures = figures
        self.set1 = set1
        self.set2 = set2

        self.initUI()

    def setFigures(self, f):
        self.figures = f

    def paintEvent(self, QPaintEvent):
        self.drawPlane()

    def addFigure(self, twoCircles):
        self.figures.append(twoCircles)

    def initUI(self):
        self.pannel.setGeometry(0, 0, self.sizeScreen[0], self.sizeScreen[1])
        self.setGeometry(0, 0, self.sizeScreen[0], self.sizeScreen[1])

        self.drawAxes()

        self.pannel.setLayout(self.layout)
        self.setWindowTitle('Lab 1')
        self.show()

    def drawPlane(self):
        self.coordinatePlane = CoordinatePlane(self.size())
        self.qp.begin(self)
        self.qp.setPen(Qt.black)

        self.drawAxes()
        self.__drawPoints()

        for i in self.figures:
            random_color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            while random_color == (255, 255, 255):
                random_color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            newPen = QPen()
            newPen.setColor(random_color)
            self.qp.setPen(newPen)

            i.draw(self.qp, self.kx, self.ky, self.dx, self.dy, self.sizeScreen)

        self.qp.end()

    def __drawPoints(self):
        color = Qt.red
        newPen = QPen()
        newPen.setColor(color)
        self.qp.setPen(newPen)
        for i in range(len(self.set1)):
            point = QPoint((self.set1[i].get_x() + self.dx) * self.kx, self.sizeScreen[1] - (self.set1[i].get_y() + self.dy) * self.ky)
            self.qp.drawEllipse(point, 5, 5)
            point = QPoint(round(point.x() - 20), round((point.y() - 20)))
            text = ""
            text += str(self.set1[i].get_x()) + "," + str(self.set1[i].get_y())
            self.qp.drawStaticText(point, QStaticText(text))

        color = Qt.green
        newPen = QPen()
        newPen.setColor(color)
        self.qp.setPen(newPen)
        for i in range(len(self.set2)):
            point = QPoint((self.set2[i].get_x() + self.dx) * self.kx, self.sizeScreen[1] - (self.set2[i].get_y() + self.dy) * self.ky)
            self.qp.drawEllipse(point, 5, 5)
            point = QPoint(round(point.x() - 20), round((point.y() - 20)))
            text = ""
            text += str(self.set2[i].get_x()) + "," + str(self.set2[i].get_y())
            self.qp.drawStaticText(point, QStaticText(text))

    def __randomColor(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def drawAxes(self):

        xMax, yMax, xMin, yMin = self.__getBounds()

        resize = 10

        if abs(xMax) < 1 or abs(yMax) < 1 or abs(xMin) < 1 or abs(yMin) < 1:
            resize = 0.5
        if abs(xMax) / 10 < 1 or abs(yMax) / 10 < 1 or abs(xMin) / 10 < 1 or abs(yMin) / 10 < 1:
            resize = 0.1

        xMin -= resize
        yMin -= resize

        self.dx = -1 * xMin
        self.dy = -1 * yMin

        intervalX = (xMax + resize) - xMin
        intervalY = (yMax + resize) - yMin

        k = min((self.sizeScreen[0] - resize) / (intervalX), (self.sizeScreen[1] - resize) / (intervalY))

        self.kx = k
        self.ky = k

        stepX = (intervalX / 10)
        stepY = (intervalY / 10)

        self.qp.drawLine(1, 0, 1, self.sizeScreen[1])
        self.qp.drawLine(0, self.sizeScreen[1] - 2, self.sizeScreen[0], self.sizeScreen[1] - 2)

        i = yMin + stepY
        while i <= self.sizeScreen[1] / self.ky:
            self.qp.drawLine(0, self.sizeScreen[1] - (i + self.dy) * self.ky, 10,
                             self.sizeScreen[1] - (i + self.dy) * self.ky)
            self.qp.drawStaticText(12, self.sizeScreen[1] - (i + self.dy) * self.ky, QStaticText(str(round(i, 2))))
            i += stepY

        i = xMin + stepX
        while i <= self.sizeScreen[0] / self.kx:
            self.qp.drawLine((i + self.dx) * self.kx, self.sizeScreen[1] - 1, (i + self.dx) * self.kx,
                             self.sizeScreen[1] - 11)
            self.qp.drawStaticText((i + self.dx) * self.kx, self.sizeScreen[1] - 25, QStaticText(str(round(i, 2))))
            i += stepX

        # for i in range(yMin + stepY, self.sizeScreen[1], stepY):
        #     self.qp.drawLine(0, self.sizeScreen[1] - (i + self.dy) * self.ky, 10, self.sizeScreen[1] - (i + self.dy) * self.ky)
        #     self.qp.drawStaticText(12, self.sizeScreen[1] - (i + self.dy) * self.ky, QStaticText(str(i)))
        #
        # for i in range(xMin + stepX, self.sizeScreen[0], stepX):
        #     self.qp.drawLine((i + self.dx) * self.kx, self.sizeScreen[1] - 1, (i + self.dx) * self.kx, self.sizeScreen[1] - 11)
        #     self.qp.drawStaticText((i + self.dx) * self.kx, self.sizeScreen[1] - 25, QStaticText(str(i)))

        # self.qp.drawStaticText(7, 7, QStaticText(str(start)))

    def __getBounds(self):
        xMax, yMax, xMin, yMin = None, None, None, None
        for i in range(len(self.figures)):
            c1, c2, r1, r2 = self.figures[i].getCircles()

            xMaxTmp = max((c1.get_x() + r1), (c2.get_x() + r2))
            xMinTmp = min((c1.get_x() - r1), (c2.get_x() - r2))
            yMaxTmp = max((c1.get_y() + r1), (c2.get_y() + r2))
            yMinTmp = min((c1.get_y() - r1), (c2.get_y() - r2))

            # xMaxTmp = max(round(c1.get_x() + r1), round(c2.get_x() + r2))
            # xMinTmp = min(round(c1.get_x() - r1), round(c2.get_x() - r2))
            # yMaxTmp = max(round(c1.get_y() + r1), round(c2.get_y() + r2))
            # yMinTmp = min(round(c1.get_y() - r1), round(c2.get_y() - r2))

            if xMax == None:
                xMax = xMaxTmp
            else:
                xMax = max(xMax, xMaxTmp)

            if yMax == None:
                yMax = yMaxTmp
            else:
                yMax = max(yMax, yMaxTmp)

            if xMin == None:
                xMin = xMinTmp
            else:
                xMin = min(xMin, xMinTmp)

            if yMin == None:
                yMin = yMinTmp
            else:
                yMin = min(yMin, yMinTmp)

        return xMax, yMax, xMin, yMin
