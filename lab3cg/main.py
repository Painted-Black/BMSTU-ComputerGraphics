from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QColorDialog, QDesktopWidget, QErrorMessage
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QColor
import sys

from mainwindow import Ui_MainWindow
from Drawing import *
from Segment import *
from SegmentSpectrum import *
from Algorithm import *


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.size = QDesktopWidget().availableGeometry()

        self.algorithms = ["ЦДА",
                           "Брезенхем с действит. числами",
                           "Брезенхем с целыми числами",
                           "Брезенхем с устранением ступенчатости",
                           "Библиотечный (PyQt5)"]

        self.singleColor = QColor(Qt.black)
        self.spectrumColor = QColor(Qt.black)

        self.singleAlgorithm = Algorithm.DDA
        self.spectrumAlgorithm = Algorithm.DDA

        self.__adjustWidgets()


    def __adjustWidgets(self):
        self.ui.button_chose_spec_color.clicked.connect(self.choseSpecColor)
        self.ui.colorButton.clicked.connect(self.choseColor)
        self.ui.showButton.clicked.connect(self.drawSingle)
        self.ui.button_draw_spec.clicked.connect(self.drawSpectrum)

        self.ui.combobox_alg_single.addItems(self.algorithms)
        self.ui.combobox_alg_spec.addItems(self.algorithms)

        self.ui.spin_box_xs.setMinimum(0)
        self.ui.spin_box_xs.setMaximum(self.size.width())
        self.ui.spin_box_xe.setMinimum(0)
        self.ui.spin_box_xe.setMaximum(self.size.width())

        self.ui.spin_box_ys.setMinimum(0)
        self.ui.spin_box_ys.setMaximum(self.size.width())
        self.ui.spin_box_ye.setMinimum(0)
        self.ui.spin_box_ye.setMaximum(self.size.width())

        self.ui.spin_box_len.setMinimum(1)
        self.ui.spin_box_len.setMaximum(self.size.height() / 2 - 20)
        self.ui.spin_box_step.setMinimum(1)
        self.ui.spin_box_step.setMaximum(180)

    def choseSpecColor(self):
        self.spectrumColor = QColorDialog.getColor()
        self.ui.widget_spec_color.setStyleSheet("QWidget { background-color: %s }" % self.spectrumColor.name())

    def drawSpectrum(self):
        len = self.ui.spin_box_len.value()
        step = self.ui.spin_box_step.value()
        self.spectrumAlgorithm = self.getAlg(self.ui.combobox_alg_spec.currentText())

        drawableObject = SegmentSpectrum(len, step, True, self.spectrumAlgorithm, self.spectrumColor)
        self.newWindowSpec = Drawing(drawableObject)
        self.newWindowSpec.show()

    def drawSingle(self):
        xs = self.ui.spin_box_xs.value()
        ys = self.ui.spin_box_ys.value()
        xe = self.ui.spin_box_xe.value()
        ye = self.ui.spin_box_ye.value()

        self.singleAlgorithm = self.getAlg(self.ui.combobox_alg_single.currentText())

        if QPoint(xs, ys) != QPoint(xe, ye):
            drawableObject = Segment(xs, ys, xe, ye, self.singleAlgorithm, self.singleColor)
            self.newWindow = Drawing(drawableObject)
            self.newWindow.show()
        else:
            self.__showErrorMessage("Начало и конец отрезка совпадают!")

    def getAlg(self, string):
        if string == self.algorithms[0]:
            return Algorithm.DDA
        elif string == self.algorithms[1]:
            return Algorithm.BRN
        elif string == self.algorithms[2]:
            return Algorithm.BIN
        elif string == self.algorithms[3]:
            return Algorithm.BAA
        elif string == self.algorithms[4]:
            return Algorithm.LA

    def choseColor(self):
        self.singleColor = QColorDialog.getColor()
        self.ui.widget_color.setStyleSheet("QWidget { background-color: %s }" % self.singleColor.name())

    def __showErrorMessage(self, message):
        error_message = QErrorMessage(self)
        error_message.setWindowTitle("Error")
        error_message.showMessage(message)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
