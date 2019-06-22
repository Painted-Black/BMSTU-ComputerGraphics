# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(255, 371)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.Single = QtWidgets.QWidget()
        self.Single.setObjectName("Single")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Single)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label_xs = QtWidgets.QLabel(self.Single)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_xs.setFont(font)
        self.label_xs.setObjectName("label_xs")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_xs)
        self.spin_box_xs = QtWidgets.QSpinBox(self.Single)
        self.spin_box_xs.setMaximum(1000)
        self.spin_box_xs.setObjectName("spin_box_xs")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spin_box_xs)
        self.label_ys = QtWidgets.QLabel(self.Single)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ys.setFont(font)
        self.label_ys.setObjectName("label_ys")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_ys)
        self.spin_box_ys = QtWidgets.QSpinBox(self.Single)
        self.spin_box_ys.setObjectName("spin_box_ys")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spin_box_ys)
        self.label_xe = QtWidgets.QLabel(self.Single)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_xe.setFont(font)
        self.label_xe.setObjectName("label_xe")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_xe)
        self.spin_box_xe = QtWidgets.QSpinBox(self.Single)
        self.spin_box_xe.setObjectName("spin_box_xe")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spin_box_xe)
        self.label_ye = QtWidgets.QLabel(self.Single)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ye.setFont(font)
        self.label_ye.setObjectName("label_ye")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_ye)
        self.spin_box_ye = QtWidgets.QSpinBox(self.Single)
        self.spin_box_ye.setObjectName("spin_box_ye")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spin_box_ye)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.combobox_alg_single = QtWidgets.QComboBox(self.Single)
        self.combobox_alg_single.setObjectName("combobox_alg_single")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.combobox_alg_single)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.widget_color = QtWidgets.QWidget(self.Single)
        self.widget_color.setMinimumSize(QtCore.QSize(20, 20))
        self.widget_color.setStyleSheet("background-color: black")
        self.widget_color.setObjectName("widget_color")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.widget_color)
        self.colorButton = QtWidgets.QPushButton(self.Single)
        self.colorButton.setObjectName("colorButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.colorButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.showButton = QtWidgets.QPushButton(self.Single)
        self.showButton.setObjectName("showButton")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.showButton)
        spacerItem3 = QtWidgets.QSpacerItem(10, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.tabWidget.addTab(self.Single, "")
        self.Spectrum = QtWidgets.QWidget()
        self.Spectrum.setObjectName("Spectrum")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Spectrum)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.combobox_alg_spec = QtWidgets.QComboBox(self.Spectrum)
        self.combobox_alg_spec.setObjectName("combobox_alg_spec")
        self.verticalLayout_3.addWidget(self.combobox_alg_spec)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setContentsMargins(11, 11, 11, 11)
        self.formLayout_3.setSpacing(6)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_length = QtWidgets.QLabel(self.Spectrum)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_length.setFont(font)
        self.label_length.setObjectName("label_length")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_length)
        self.spin_box_len = QtWidgets.QSpinBox(self.Spectrum)
        self.spin_box_len.setObjectName("spin_box_len")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spin_box_len)
        self.label_step = QtWidgets.QLabel(self.Spectrum)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_step.setFont(font)
        self.label_step.setObjectName("label_step")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_step)
        self.spin_box_step = QtWidgets.QSpinBox(self.Spectrum)
        self.spin_box_step.setObjectName("spin_box_step")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spin_box_step)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem5)
        self.button_draw_spec = QtWidgets.QPushButton(self.Spectrum)
        self.button_draw_spec.setObjectName("button_draw_spec")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.button_draw_spec)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem6)
        self.button_chose_spec_color = QtWidgets.QPushButton(self.Spectrum)
        self.button_chose_spec_color.setObjectName("button_chose_spec_color")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.button_chose_spec_color)
        self.widget_spec_color = QtWidgets.QWidget(self.Spectrum)
        self.widget_spec_color.setMinimumSize(QtCore.QSize(20, 20))
        self.widget_spec_color.setStyleSheet("background-color: black")
        self.widget_spec_color.setObjectName("widget_spec_color")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.widget_spec_color)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem7)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        self.tabWidget.addTab(self.Spectrum, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 255, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_xs.setText(_translate("MainWindow", "Xs"))
        self.label_ys.setText(_translate("MainWindow", "Ys"))
        self.label_xe.setText(_translate("MainWindow", "Xe"))
        self.label_ye.setText(_translate("MainWindow", "Ye"))
        self.colorButton.setText(_translate("MainWindow", "Chose color"))
        self.showButton.setText(_translate("MainWindow", "Show"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Single), _translate("MainWindow", "Single Section"))
        self.label_length.setText(_translate("MainWindow", "Radius"))
        self.label_step.setText(_translate("MainWindow", "Step"))
        self.button_draw_spec.setText(_translate("MainWindow", "Show"))
        self.button_chose_spec_color.setText(_translate("MainWindow", "Chose color"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Spectrum), _translate("MainWindow", "Spectrum"))

