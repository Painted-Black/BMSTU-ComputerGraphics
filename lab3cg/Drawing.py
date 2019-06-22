from PyQt5.QtWidgets import QWidget, QGridLayout, QDesktopWidget
from PyQt5.QtGui import QPainter, QStaticText
from PyQt5.QtCore import Qt, QRect

from CoordinatePlane import *


class Drawing(QWidget):

    def __init__(self, object):
        super().__init__()

        self.pannel = QWidget(self)
        self.layout = QGridLayout()
        self.qp = QPainter()
        self.sizeScreen = self.__getSize()
        self.coordinatePlane = None

        self.drawableObject = object

        self.initUI()

    def initUI(self):
        self.pannel.setGeometry(QRect(0, 0, self.sizeScreen[0], self.sizeScreen[1]))
        self.setGeometry(QRect(0, 0, self.sizeScreen[0], self.sizeScreen[1]))

        self.drawAxes()

        self.pannel.setLayout(self.layout)
        self.setWindowTitle('Lab 3')
        self.show()

    def drawAxes(self):
        self.qp.drawLine(0, 1, self.sizeScreen[0], 1)
        self.qp.drawLine(1, 0, 1, self.sizeScreen[1])

        for i in range(100, self.sizeScreen[0], 100):
            self.qp.drawLine(i, 0, i, 7)
            self.qp.drawStaticText(i - 10, 7, QStaticText(str(i)))

        for i in range(100, self.sizeScreen[1], 100):
            self.qp.drawLine(0, i, 10, i)
            self.qp.drawStaticText(10, i - 10, QStaticText(str(i)))

    def paintEvent(self, QPaintEvent):
        self.drawPlane()

    def drawPlane(self):
        self.coordinatePlane = CoordinatePlane(self.size())
        self.qp.begin(self)
        self.qp.setPen(Qt.black)
        self.drawAxes()
        self.drawableObject.draw(self.sizeScreen, self.qp)

        self.qp.end()

    def __getSize(self):
        h = QDesktopWidget().screenGeometry().height() - 100
        w = QDesktopWidget().screenGeometry().width() - 100
        return [w, h]
