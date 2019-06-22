from PyQt5.QtWidgets import QPlainTextEdit, QGridLayout, QWidget, QDesktopWidget, QPushButton, QLabel, QMessageBox, \
                            QRadioButton, QButtonGroup, QTextEdit, QDoubleSpinBox
from PyQt5.QtGui import QFont, QPainter, QPen, QPalette, QTransform, QValidator, QRegExpValidator, QColor, QStaticText
from PyQt5.QtWidgets import QErrorMessage
from CoordinatePlane import *
from PyQt5.QtCore import Qt, QRect, QRegExp, QEvent, QPoint
from math import radians, sin, cos, degrees, sqrt
from Point import *
from TangentPosition import *
from TwoCircles import *
import random
from Drawing import *
from Point import *

class Mainframe(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        self.pannel = QWidget(self)
        self.qp = QPainter()
        self.sizeScreen = QDesktopWidget().availableGeometry()

        self.newWindow = None

        self.figures = []

        self.set1 = []
        self.set2 = []

        self.newWindow = None

        self.textEdit1 = QTextEdit()
        self.textEdit2 = QTextEdit()

        self.text_edit_x = QDoubleSpinBox()
        self.text_edit_change_x = QDoubleSpinBox()
        self.text_edit_y = QDoubleSpinBox()
        self.text_edit_change_y = QDoubleSpinBox()

        self.button_add = QPushButton("Добавить")
        self.button_find = QPushButton("Ответ")
        self.button_delete_all = QPushButton("Удалить все")
        self.button_change = QPushButton("Изменить точку")
        self.button_delete = QPushButton("Удалить")

        self.radio_button_1 = QRadioButton("set 1")
        self.radio_button_2 = QRadioButton("set 2")
        self.radio_group = QButtonGroup()

        self.label_x = QLabel("x")
        self.label_y = QLabel("y")
        self.label_set1 = QLabel("Set 1")
        self.label_set2 = QLabel("Set 2")

        self.__adjustWidgets()

        self.initUI()

    def __adjustWidgets(self):
        self.textEdit1.setReadOnly(True)
        self.textEdit2.setReadOnly(True)

        self.text_edit_x.setMinimum(-1 * self.sizeScreen.width())
        self.text_edit_x.setMaximum(self.sizeScreen.width())

        self.text_edit_change_x.setMinimum(-1 * self.sizeScreen.width() - 10)
        self.text_edit_change_x.setMaximum(self.sizeScreen.width())

        self.text_edit_y.setMinimum(-1 * self.sizeScreen.height())
        self.text_edit_y.setMaximum(self.sizeScreen.height())

        self.text_edit_change_y.setMinimum(-1 * self.sizeScreen.height())
        self.text_edit_change_y.setMaximum(self.sizeScreen.height())

        self.radio_group.addButton(self.radio_button_1)
        self.radio_group.addButton(self.radio_button_2)

        self.button_add.clicked.connect(self.__OnAddClicked)
        self.button_find.clicked.connect(self.__OnFindClicked)
        self.button_change.clicked.connect(self.__buttonChangeEvent)
        self.button_delete.clicked.connect(self.__deletePoint)
        self.button_delete_all.clicked.connect(self.__deleteAllButtonEvent)

    def __deletePoint(self):
        cursor1 = self.textEdit1.textCursor()
        cursor2 = self.textEdit2.textCursor()

        textSelected1 = cursor1.selectedText()
        textSelected2 = cursor2.selectedText()

        textSelected1.strip()
        textSelected2.strip()

        x1, y1 = self.__isPoinFormat(textSelected1)
        x2, y2 = self.__isPoinFormat(textSelected2)

        if x1 != None and y1 != None:
            idx = self.getIndex(self.set1, MyPoint(x1, y1))
            self.set1.pop(idx)
            self.__fillEditText(self.textEdit1, self.set1)
        elif x2 != None and y2 != None:
            idx = self.getIndex(self.set2, MyPoint(x2, y2))
            self.set2.pop(idx)
            self.__fillEditText(self.textEdit2, self.set2)

    def getIndex(self, set, point):
        for i in range(len(set)):
            if set[i].get_x() == point.get_x() and set[i].get_y() == point.get_y():
                return i
        return -1

    def __buttonChangeEvent(self):
        cursor1 = self.textEdit1.textCursor()
        cursor2 = self.textEdit2.textCursor()

        textSelected1 = cursor1.selectedText()
        textSelected2 = cursor2.selectedText()

        x1, y1 = self.__isPoinFormat(textSelected1)
        x2, y2 = self.__isPoinFormat(textSelected2)
        newX = self.text_edit_change_x.value()
        newY = self.text_edit_change_y.value()

        newPoint = MyPoint(newX, newY)

        if x1 != None and y1 != None:
            point1 = MyPoint(x1, y1)
            if not self.__isIn(self.set1, newPoint):
                self.__replacePoint(point1, newPoint, self.set1)
                self.__fillEditText(self.textEdit1, self.set1)
        elif x2 != None and y2 != None:
            point2 = MyPoint(x2, y2)
            if not self.__isIn(self.set2, newPoint):
                self.__replacePoint(point2, newPoint, self.set2)
                self.__fillEditText(self.textEdit2, self.set2)

    def __replacePoint(self, oldPoint, newPoint, set):
        for i in range(len(set)):
            if set[i].get_x() == oldPoint.get_x() and set[i].get_y() == oldPoint.get_y():
                set[i].set_x(newPoint.get_x())
                set[i].set_y(newPoint.get_y())

    def __isPoinFormat(self, text):
        text = text.__str__()
        splited = text.split(',')
        if len(splited) == 2:
            splited[0].strip()
            splited[1].strip()
            try:
                return float(splited[0]), float(splited[1])
            except ValueError:
                return None, None
        return None, None

    def __isInt(self, str):
        return true

    def __isIn(self, set, point):
        for i in range(len(set)):
            if set[i].get_x() == point.get_x() and set[i].get_y() == point.get_y():
                return True
        return False

    def __OnAddClicked(self):
        x = self.text_edit_x.value()
        y = self.text_edit_y.value()
        newPoint = MyPoint(x, y)
        if self.radio_button_1.isChecked() and not self.__isIn(self.set1, newPoint):
            self.set1.append(newPoint)
            str = ""
            str += (newPoint.get_x()).__str__()
            str += ','
            str += (newPoint.get_y()).__str__()
            self.textEdit1.append(str)
        elif self.radio_button_2.isChecked() and not self.__isIn(self.set2, newPoint):
            self.set2.append(newPoint)
            str = ""
            str += (newPoint.get_x()).__str__()
            str += ','
            str += (newPoint.get_y()).__str__()
            self.textEdit2.append(str)

    def __fillEditText(self, textEdit, set):
        textEdit.clear()
        text = ""
        for i in range(len(set)):
            text += str(set[i].get_x())
            text += ","
            text += str(set[i].get_y())
            #text += "\n"
            textEdit.append(text)
            text = ""
        #textEdit.setPlainText(text)

    def initUI(self):
        self.pannel.setGeometry(QRect(0, 0, 400, 500))
        self.setGeometry(0, 0, 400, 500)

        self.__addWidgets()

        self.pannel.setLayout(self.layout)
        self.setWindowTitle('Lab 1')
        self.show()

    def __clearInput(self):
        self.textEdit1.clear()
        self.textEdit2.clear()
        self.set1.clear()
        self.set2.clear()

    # def __clearDrawing(self):
    #     self.figures.clear()


    def __OnFindClicked(self):
        self.figures.clear()
        self.__findPoints(self.set1, self.set2)
        if len(self.figures):

            self.newWindow = Drawing(self.figures, self.set1, self.set2)
            # self.newWindow.setFigures(self.figures)
            self.newWindow.show()
        else:
            self.__showErrorMessage("Ничего не найдено!")

    def __deleteAllButtonEvent(self):
        self.__clearInput()

    def __parseText(self):
        self.__findPoints(set1, set2)

    def findCenter(self, p1, p2, p3):
        A = 2 * (p2.get_x() - p1.get_x())
        B = 2 * (p2.get_y() - p1.get_y())
        C = (p2.get_x() ** 2) - (p1.get_x() ** 2) + (p2.get_y() ** 2) - (p1.get_y() ** 2)
        D = 2 * (p3.get_x() - p2.get_x())
        E = 2 * (p3.get_y() - p2.get_y())
        F = (p3.get_x() ** 2) - (p2.get_x() ** 2) + (p3.get_y() ** 2) - (p2.get_y() ** 2)

        x0 = round((C * E - B * F) / (A * E - B * D), 2)
        y0 = round((A * F - D * C) / (A * E - D * B), 2)
        return MyPoint(x0, y0)

    def findRadius(self, center, p):
        a = (p.get_x() - center.get_x()) ** 2 + (p.get_y() - center.get_y()) ** 2
        rad = sqrt((p.get_x() - center.get_x()) ** 2 + (p.get_y() - center.get_y()) ** 2)
        return rad

    def __findPoints(self, set1, set2):
        for i in range(len(set1)):
            for j in range(i + 1, len(set1)):
                for k in range(i + 2, len(set1)):
                    if not self.__isPointsInOneLine(set1[i], set1[j], set1[k]):
                        for i2 in range(len(set2)):
                            for j2 in range(i2 + 1, len(set2)):
                                for k2 in range(i2 + 2, len(set2)):
                                    if not self.__isPointsInOneLine(set2[i2], set2[j2], set2[k2]):

                                        point11 = MyPoint(set1[i].get_x(), set1[i].get_y())
                                        point12 = MyPoint(set1[j].get_x(), set1[j].get_y())
                                        point13 = MyPoint(set1[k].get_x(), set1[k].get_y())

                                        point21 = MyPoint(set2[i2].get_x(), set2[i2].get_y())
                                        point22 = MyPoint(set2[j2].get_x(), set2[j2].get_y())
                                        point23 = MyPoint(set2[k2].get_x(), set2[k2].get_y())

                                        center1 = self.findCenter(point11, point12, point13)
                                        center2 = self.findCenter(point21, point22, point23)

                                        rad1 = round(self.findRadius(center1, point11), 2)
                                        rad2 = round(self.findRadius(center2, point21), 2)
                                        self.__checkCircles(center1, center2, rad1, rad2)

    def addCircles(self, c1, c2, r1, r2, position):
        a = 1
        n = TwoCircles(c1, c2, r1, r2, position)
        self.figures.append(n)

    def __randomColor(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def __checkCircles(self, c1, c2, r1, r2):
        if c1.get_x() == c2.get_x() and c1.get_y() == c2.get_y() and r1 != r2:
            return False
        max_y1 = c1.get_y() + r1
        max_y2 = c2.get_y() + r2
        min_y1 = c1.get_y() - r1
        min_y2 = c2.get_y() - r2
        position = None
        if max_y1 == max_y2:
            position = (MyPoint(c1.get_x(), max_y1),
                        MyPoint(c2.get_x(), max_y2)) #TangentPosition.downDown
        # elif max_y1 == min_y2:
        #     position =  (MyPoint(c1.get_x(), max_y1),
        #                  MyPoint(c2.get_x(), min_y2))#TangentPosition.downUp
        elif min_y1 == min_y2:
            position = (MyPoint(c1.get_x(), min_y1),
                        MyPoint(c2.get_x(), min_y2)) #TangentPosition.upUp
        # elif min_y1 == max_y2:
        #     position = (MyPoint(c1.get_x(), min_y1),
        #                 MyPoint(c2.get_x(), max_y2)) #TangentPosition.upDown

        if (position != None):
            self.addCircles(c1, c2, r1, r2, position)

    def __isPointsInOneLine(self, p1, p2, p3):
        return ((p2.get_y() - p1.get_y()) * (p3.get_x() - p1.get_x()) == (p3.get_y() - p1.get_y()) * (p2.get_x() - p1.get_x()))
        #return (p1.get_y() - p2.get_y()) * p3.get_x() + (p2.get_x() - p1.get_x()) * p3.get_y() + (p1.get_x() * p2.get_y() - p2.get_x() * p1.get_y()) == 0

    def __toCoordFormat(self, set):
        message = ""
        res = []
        for i in range(0, len(set)):
            tmp = set[i].split(',')
            if len(tmp) == 2 and tmp[0].isdecimal() and tmp[1].isdecimal():
                res.append([float(tmp[0]), float(tmp[1])])
            else:
                if len(tmp) != 2:
                    message = "Incorrect input!"
                if tmp[0].isdecimal() and tmp[1].isdecimal():
                    message = "You must imput at least 3 points in each set!"
                return None, message
        return res, message

    def __checkPointFormat(self, arr):
        for i in range(0, len(arr)):
            splitArr = arr[i].split(',')
            if len(splitArr) == 2 and splitArr[0].isdecimal() and splitArr[1].isdecimal():
                continue
            return False
        return True

    def __infoButtonEvent(self):
        self.__showMessage(self.info)

    def __addWidgets(self):
        self.layout.addWidget(self.label_set1, 0, 0)
        self.layout.addWidget(self.label_set2, 0, 1)
        self.layout.addWidget(self.textEdit1, 1, 0)
        self.layout.addWidget(self.textEdit2, 1, 1)

        self.layout.addWidget(self.button_add, 2, 0)
        self.layout.addWidget(self.text_edit_x, 2, 1)
        self.layout.addWidget(QLabel("x"), 2, 2)
        self.layout.addWidget(self.text_edit_y, 3, 1)
        self.layout.addWidget(QLabel("y"), 3, 2)
        self.layout.addWidget(QLabel("set"), 4, 0)
        self.layout.addWidget(self.radio_button_1, 4, 1)
        self.layout.addWidget(self.radio_button_2, 5, 1)

        self.layout.addWidget(self.button_find, 6, 0)
        self.layout.addWidget(self.button_change, 7, 0)
        self.layout.addWidget(self.text_edit_change_x, 7, 1)
        self.layout.addWidget(QLabel("x"), 7, 2)
        self.layout.addWidget(self.text_edit_change_y, 8, 1)
        self.layout.addWidget(QLabel("y"), 8, 2)

        self.layout.addWidget(self.button_delete, 9, 0)
        self.layout.addWidget(self.button_delete_all, 10, 0)

    # def __showMessage(self, message):
    #     message_box = QMessageBox.information(self, "Info", message)

    def __showErrorMessage(self, message):
        error_message = QErrorMessage(self)
        error_message.setWindowTitle("Error")
        error_message.showMessage(message)

    def paintEvent(self, e):
        self.drawPlane()

    # def drawAxes(self):
    #     self.qp.drawLine(10,0, 10, self.sizeScreen.height())

    def drawPlane(self):
        self.coordinatePlane = CoordinatePlane(self.size())
        self.qp.begin(self)
        self.qp.setPen(Qt.black)

        self.qp.end()
