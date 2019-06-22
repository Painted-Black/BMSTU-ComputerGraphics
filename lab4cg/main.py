from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QColorDialog, QErrorMessage
import sys

from mainwindow import Ui_MainWindow
from Drawing import *
from CircleSpectrum import *
from EllipseSpectrum import *


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        alg = Algorithm.CANON_EQ
        self.circleAlgorithms = alg.getArray()
        self.ellipseAlgorithms = alg.getArray()

        self.size = QDesktopWidget().availableGeometry()

        self.circleColor = QColor(Qt.black)
        self.circleBgColor = QColor(Qt.white)
        self.ellipseColor = QColor(Qt.black)
        self.ellipseBgColor = QColor(Qt.white)

        self.childWindow = None

        self.__adjustWidgets()

    def __adjustWidgets(self):
        self.ui.spin_box_ycenter_circle.setMinimum(0)
        self.ui.spin_box_xcenter_circle.setMaximum(self.size.width())
        self.ui.spin_box_ycenter_circle.setMinimum(0)
        self.ui.spin_box_ycenter_circle.setMaximum(self.size.height())
        self.ui.spin_box_circle_radius.setMinimum(1)
        self.ui.spin_box_circle_radius.setMaximum(self.size.height())
        self.ui.spinBox_circle_number.setMinimum(1)
        self.ui.spinBox_circle_number.setMaximum(500)
        self.ui.spinBox_circle_step.setMinimum(1)
        self.ui.spinBox_circle_step.setMaximum(self.size.height())

        self.ui.spinBox_ellipse_xc.setMinimum(0)
        self.ui.spinBox_ellipse_xc.setMaximum(self.size.width())
        self.ui.spinBox_ellipse_yc.setMinimum(0)
        self.ui.spinBox_ellipse_yc.setMaximum(self.size.height())

        self.ui.combobox_alg_circle.addItems(self.circleAlgorithms)

        self.ui.spinBox_start_semiaxis_x.setMinimum(1)
        self.ui.spinBox_start_semiaxis_x.setMaximum(self.size.height())
        self.ui.spinBox_start_semiaxis_y.setMinimum(1)
        self.ui.spinBox_start_semiaxis_y.setMaximum(self.size.height())
        self.ui.spinBox_ellipse_number.setMinimum(1)
        self.ui.spinBox_ellipse_number.setMaximum(500)
        self.ui.spin_box_ellipse_step_x.setMinimum(1)
        self.ui.spin_box_ellipse_step_x.setMaximum(self.size.height())
        self.ui.spinBox_ellipse_step_y.setMinimum(1)
        self.ui.spinBox_ellipse_step_y.setMaximum(self.size.height())

        self.ui.comboBox_ellipse_alg.addItems(self.ellipseAlgorithms)

        self.ui.button_circle_color.clicked.connect(lambda x:
                                                    self.choseCircleColor(self.ui.widget_circle_color))
        self.ui.button_circle_bg_color.clicked.connect(lambda x:
                                                       self.choseCircleBgColor(self.ui.widget_circle_bg_color))
        self.ui.button_chose_ellipse_color.clicked.connect(lambda x:
                                                           self.choseEllipseColor(self.ui.widget_ellipse_color))
        self.ui.button_ellipse_bg_color.clicked.connect(lambda x:
                                                        self.choseEllipseBgColor(self.ui.widget_ellipse_bg_color))
        self.ui.showCircleButton.clicked.connect(self.__drawCircle)
        self.ui.button_draw_ellipse_spec.clicked.connect(self.__drawEllipse)

    def __showErrorMessage(self, message):
        error_message = QErrorMessage(self)
        error_message.setWindowTitle("Error")
        error_message.showMessage(message)

    def choseEllipseBgColor(self, widget):
        self.ellipseBgColor = self.choseColor()
        if widget is not None:
            widget.setStyleSheet("QWidget { background-color: %s }" % self.ellipseBgColor.name())

    def choseEllipseColor(self, widget):
        self.ellipseColor = self.choseColor()
        if widget is not None:
            widget.setStyleSheet("QWidget { background-color: %s }" % self.ellipseColor.name())

    def choseCircleBgColor(self, widget):
        self.circleBgColor = self.choseColor()
        if widget is not None:
            widget.setStyleSheet("QWidget { background-color: %s }" % self.circleBgColor.name())

    def choseCircleColor(self, widget):
        self.circleColor = self.choseColor()
        if widget is not None:
            widget.setStyleSheet("QWidget { background-color: %s }" % self.circleColor.name())

    def choseColor(self):
        newColor = QColorDialog.getColor()
        return newColor

    def __drawCircle(self):
        if self.circleColor == self.circleBgColor:
            self.__showErrorMessage("Цвет фона и цвет рисунка совпадают!")
            return
        xc = self.ui.spin_box_xcenter_circle.value()
        yc = self.ui.spin_box_ycenter_circle.value()
        start_radius = self.ui.spin_box_circle_radius.value()
        count = self.ui.spinBox_circle_number.value()
        step = self.ui.spinBox_circle_step.value()
        alg = self.__getAlgorithm(self.ui.combobox_alg_circle.currentText())

        drawableObject = CircleSpectrum(QPoint(xc, yc), start_radius, count, step, alg, self.circleColor)
        self.childWindow = Drawing(drawableObject, self.circleBgColor, self.circleColor)
        self.childWindow.show()

    def __drawEllipse(self):
        if self.ellipseColor == self.ellipseBgColor:
            self.__showErrorMessage("Цвет фона и цвет рисунка совпадают!")
            return
        xc = self.ui.spinBox_ellipse_xc.value()
        yc = self.ui.spinBox_ellipse_yc.value()
        axisX = self.ui.spinBox_start_semiaxis_x.value()
        axisY = self.ui.spinBox_start_semiaxis_y.value()
        count = self.ui.spinBox_ellipse_number.value()
        stepX = self.ui.spin_box_ellipse_step_x.value()
        stepY = self.ui.spinBox_ellipse_step_y.value()
        alg = self.__getAlgorithm(self.ui.comboBox_ellipse_alg.currentText())

        drawableObject = EllipseSpectrum(QPoint(xc, yc), axisX, axisY, count, stepX, stepY, alg, self.ellipseColor)
        self.childWindow = Drawing(drawableObject, self.ellipseBgColor, self.ellipseColor)
        self.childWindow.show()

    def __getAlgorithm(self, stringAlgName):
        if stringAlgName == Algorithm.CANON_EQ.value:
            return Algorithm.CANON_EQ
        elif stringAlgName == Algorithm.PARA_EQ.value:
            return Algorithm.PARA_EQ
        elif stringAlgName == Algorithm.BRESENHAM_ALG.value:
            return Algorithm.BRESENHAM_ALG
        elif stringAlgName == Algorithm.MIDDLE_DOT_ALG.value:
            return Algorithm.MIDDLE_DOT_ALG
        elif stringAlgName == Algorithm.LIBRARY_ARG.value:
            return Algorithm.LIBRARY_ARG


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
