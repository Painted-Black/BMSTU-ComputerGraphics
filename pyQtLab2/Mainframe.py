# from PyQt5.QtWidgets import QWidget, QPushButton, QToolTip, QDesktopWidget
from PyQt5.QtWidgets import QWidget, QPushButton, QToolTip, QVBoxLayout, QHBoxLayout, \
     QDesktopWidget, QLineEdit, QLabel, QGridLayout, QDoubleSpinBox, QSpinBox, QErrorMessage
from PyQt5.QtGui import QFont, QPainter, QPen, QPalette, QTransform, QMatrix3x2, QStaticText
from CoordinatePlane import *
from PyQt5.QtCore import Qt, QRect, QPoint
from Include.Astroid import *
from Include.Figure import *
from Include.Circle import *
from Include.Rect import *
from math import radians, sin, cos, degrees
from Include.Action import *

class Mainframe(QWidget):

    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        self.pannel = QWidget(self)
        self.qp = QPainter()
        self.coordinatePlane = CoordinatePlane(QDesktopWidget().availableGeometry())

        self.sizeScreen = QDesktopWidget().availableGeometry()
        self.__setDefaultPosition()

        self.figures = []
        self.figures = self.__figures()

        self.label_move_dx           = QLabel("dx")
        self.label_move_dy           = QLabel("dy")
        self.label_resize_xc         = QLabel("xc")
        self.label_resize_yc         = QLabel("yc")
        self.label_resize_kx         = QLabel("kx")
        self.label_resize_ky         = QLabel("ky")
        self.label_rotate_xc         = QLabel("xc")
        self.label_rotate_yc         = QLabel("yc")
        self.label_rotate_angle      = QLabel("angle")
        self.label_move              = QLabel("Movement")
        self.label_resize            = QLabel("Resize")
        self.label_rotate            = QLabel("Rotation")

        self.button_move   = QPushButton("Move")
        self.button_resize = QPushButton("Resize")
        self.button_rotate = QPushButton("Rotate")
        self.button_reset  = QPushButton("Reset")
        self.button_back   = QPushButton("Back")

        self.button_move.clicked.connect(self.buttonMoveEvent)
        self.button_resize.clicked.connect(self.buttonResizeEvent)
        self.button_rotate.clicked.connect(self.buttonRotateEvent)
        self.button_back.clicked.connect(self.buttonBackEvent)
        self.button_reset.clicked.connect(self.buttonResetEvent)

        self.edit_move_dx   = QDoubleSpinBox()
        self.edit_move_dy   = QDoubleSpinBox()
        self.edit_resize_xc = QDoubleSpinBox()
        self.edit_resize_yc = QDoubleSpinBox()
        self.edit_resize_kx = QDoubleSpinBox()
        self.edit_resize_ky = QDoubleSpinBox()
        self.edit_rotate_xc = QDoubleSpinBox()
        self.edit_rotate_yc = QDoubleSpinBox()
        self.edit_angle = QSpinBox()

        self.edit_move_dx.setMaximum(self.sizeScreen.width() / 2)
        self.edit_move_dx.setMinimum(-1 * self.sizeScreen.width() / 2)

        self.edit_move_dy.setMaximum(self.sizeScreen.height() / 2)
        self.edit_move_dy.setMinimum(-1 * self.sizeScreen.height() / 2)

        self.edit_resize_xc.setMinimum(-1 * self.sizeScreen.width() / 2)
        self.edit_resize_xc.setMaximum(self.sizeScreen.width() / 2)

        self.edit_resize_yc.setMinimum(-1 * self.sizeScreen.height() / 2)
        self.edit_resize_yc.setMaximum(self.sizeScreen.height() / 2)

        self.edit_rotate_xc.setMaximum(self.sizeScreen.width())
        self.edit_rotate_xc.setMinimum(0)

        self.edit_rotate_yc.setMaximum(self.sizeScreen.height())
        self.edit_rotate_yc.setMinimum(0)

        self.edit_angle.setMinimum(-360)
        self.edit_angle.setMaximum(360)

        self.initUI()

    def __setDefaultPosition(self):
        self.angle             = 0
        self.rotation_center_x = 0
        self.rotation_center_y = 0
        self.radX              = 40
        self.radY              = 40
        self.astroid_heigth    = 200
        self.astroid_width     = 200
        self.rect_heigth       = 400
        self.rect_width        = 400
        self.sstate = QPoint(self.sizeScreen.width() / 2, self.sizeScreen.height() / 2)
        self.state = QPoint(self.sizeScreen.width() / 2, self.sizeScreen.height() / 2)

        self.__clearSavedState()

    def __clearSavedState(self):
        self.curRadX = None
        self.curRadY = None
        self.curAstrHeight = None
        self.curAstrWidth = None
        self.curRectH = None
        self.curRectWidth = None
        self.cur_action = None
        self.cur_angle = None
        self.cur_rotation_center_x = None
        self.cur_rotation_center_y = None
        self.cur_radX = None
        self.cur_radY = None
        self.cur_astroid_heigth = None
        self.cur_astroid_width = None
        self.cur_rect_heigth = None
        self.cur_rect_width = None
        self.cur_state = None

    def __setPreviousPosition(self):
        if (self.cur_action == None):
            self.__setDefaultPosition()
            return
        else:
            if self.cur_action == Action.MOVE:
                for i in self.figures:
                    i.move(-self.cur_dx, -self.cur_dy)
                self.repaint()
            elif self.cur_action == Action.ROTATE:
                for i in self.figures:
                    i.rotate(self.cur_rotation_center_x, self.cur_rotation_center_y,
                             -self.cur_angle)
                self.repaint()
            elif self.cur_action == Action.SCALE:
                # if (self.cur_kx != 0 and self.cur_ky != 0):
                    # for i in self.figures:
                self.figures[0].scale1(self.curRadX, self.curRadY, self.state.x(), self.state.y(), self.cur_kx, self.cur_ky)
                self.figures[1].scale1(self.curRectH, self.curRectWidth, self.state.x(), self.state.y(), self.cur_kx, self.cur_ky)
                self.figures[2].scale1(self.curAstrHeight, self.curAstrWidth, self.state.x(), self.state.y(), self.cur_kx, self.cur_ky)
                            # i.scale(1 / self.cur_kx, 1 / self.cur_ky, self.cur_scale_xc, self.cur_scale_yc)
                self.repaint()
                # else:
                #     self.__showErrorMessage("Невозможно выполнить действие!")
        self.__clearSavedState()

    def __showErrorMessage(self, message):
        error_message = QErrorMessage(self)
        error_message.setWindowTitle("Error")
        error_message.showMessage(message)

    def buttonResetEvent(self):
        self.figures = self.__figures()
        self.__clearSavedState()
        self.__setDefaultPosition()
        self.repaint()

    def buttonBackEvent(self):
        if self.cur_action != None:
            self.__setPreviousPosition()
            self.repaint()

    def buttonResizeEvent(self):
        self.kx = self.edit_resize_kx.value()
        self.ky = self.edit_resize_ky.value()
        if self.kx == 1 and self.ky == 1:
            return
        self.scale_xc = self.edit_resize_xc.value()
        self.scale_yc = self.edit_resize_yc.value()
        self.cur_action = Action.SCALE
        self.__saveScale()
        for i in self.figures:
            i.scale(self.kx, self.ky,self.scale_xc, self.scale_yc)
        self.repaint()

    def buttonRotateEvent(self):
        self.angle = self.edit_angle.value()
        if self.angle == 0:
            return
        self.rotation_center_x = self.edit_rotate_xc.value()
        self.rotation_center_y = self.edit_rotate_yc.value()
        self.cur_action = Action.ROTATE
        self.__saveRotation()
        for i in self.figures:
            i.rotate(self.rotation_center_x, self.rotation_center_y,
                     self.angle)
        self.repaint()

    def buttonMoveEvent(self):
        self.new_offset_x = self.edit_move_dx.value()
        self.new_offset_y = self.edit_move_dy.value()
        if self.new_offset_x == 0 and self.new_offset_y == 0:
            return
        self.__saveMovement()
        self.cur_action = Action.MOVE
        for i in self.figures:
            i.move(self.new_offset_x, self.new_offset_y)
        self.repaint()

    def initUI(self):
        self.pannel.setGeometry(QRect(self.sizeScreen.width() - 200, 40, 200, self.sizeScreen.height() / 2))
        self.setGeometry(0, 0, self.sizeScreen.width(), self.sizeScreen.height())

        self.__addWidgets()

        self.pannel.setLayout(self.layout)
        self.setWindowTitle('Lab 2')
        self.show()

    def __addWidgets(self):
        self.layout.addWidget(self.label_move,    0, 0)
        self.layout.addWidget(self.edit_move_dx,  1, 0)
        self.layout.addWidget(self.label_move_dx, 1, 1)
        self.layout.addWidget(self.edit_move_dy,  2, 0)
        self.layout.addWidget(self.label_move_dy, 2, 1)
        self.layout.addWidget(self.button_move,   3, 0)

        self.layout.addWidget(self.label_resize,    4, 0)
        self.layout.addWidget(self.edit_resize_xc,  5, 0)
        self.layout.addWidget(self.label_resize_xc, 5, 1)
        self.layout.addWidget(self.edit_resize_yc,  6, 0)
        self.layout.addWidget(self.label_resize_yc, 6, 1)
        self.layout.addWidget(self.edit_resize_kx,  7, 0)
        self.layout.addWidget(self.label_resize_kx, 7, 1)
        self.layout.addWidget(self.edit_resize_ky,  8, 0)
        self.layout.addWidget(self.label_resize_ky, 8, 1)
        self.layout.addWidget(self.button_resize,   9, 0)

        self.layout.addWidget(self.label_rotate,            10, 0)
        self.layout.addWidget(self.edit_rotate_xc,          11, 0)
        self.layout.addWidget(self.label_rotate_xc,         11, 1)
        self.layout.addWidget(self.edit_rotate_yc,          12, 0)
        self.layout.addWidget(self.label_rotate_yc,         12, 1)
        self.layout.addWidget(self.edit_angle,              14, 0)
        self.layout.addWidget(self.label_rotate_angle,      14, 1)
        self.layout.addWidget(self.label_rotate,            15, 0)
        self.layout.addWidget(self.button_rotate,           16, 0)

        self.layout.addWidget(self.button_back,  17, 0)
        self.layout.addWidget(self.button_reset, 18, 0)

    def paintEvent(self, e):
        self.drawPlane()

    def drawAxes(self):
        oneUnit = self.coordinatePlane.oneUnit()
        self.qp.drawLine(1, 0, 1, self.sizeScreen.height())
        self.qp.drawLine(0, 1, self.sizeScreen.width(), 1)
        for i in range(100, self.sizeScreen.height(), 100):
            self.qp.drawLine(0, i, 10, i)
            self.qp.drawStaticText(12, i - 7, QStaticText(str(i)))

        for i in range (100, self.sizeScreen.width(), 100):
            self.qp.drawLine(i, 0, i, 10)
            self.qp.drawStaticText(i - 10, 12, QStaticText(str(i)))
            self.qp.drawStaticText(7, 7, QStaticText(str(0)))


    def drawPlane(self):
        self.qp.begin(self)
        self.qp.setPen(Qt.black)
        self.drawAxes()
        self.qp.drawPoint(self.rotation_center_x, self.rotation_center_y)

        for i in self.figures:
            p = i.draw(self.coordinatePlane)
            self.qp.drawPath(p)
        self.qp.end()

    def __saveMovement(self):
        self.cur_dx = self.new_offset_x
        self.cur_dy = self.new_offset_y
        self.cur_state = self.state

    def __saveRotation(self):
        self.cur_angle = self.angle
        self.cur_rotation_center_x = self.rotation_center_x
        self.cur_rotation_center_y = self.rotation_center_y

    def __saveScale(self):
        self.curRadX = self.figures[0].x_height
        self.curRadY = self.figures[0].y_height
        self.curAstrHeight = self.astroid_heigth
        self.curAstrWidth = self.astroid_width
        self.curRectH = self.rect_heigth
        self.curRectWidth = self.rect_width
        self.state.setX(self.figures[0].center_x)
        self.state.setY(self.figures[0].center_y)
        self.cur_kx, self.cur_ky = self.kx, self.ky
        self.cur_scale_xc, self.cur_scale_yc = self.scale_xc, self.scale_yc

    def __figures(self):
        figures = []
        circle = MyCircle(self.radX, self.radY, self.sstate.x(), self.sstate.y())
        rect = Rect(self.sstate.x(), self.sstate.y(), self.rect_heigth, self.rect_width)
        ast = Astroid(self.sstate.x(), self.sstate.y(), self.astroid_heigth, self.astroid_width)
        figures.append(circle)
        figures.append(rect)
        figures.append(ast)
        return figures
