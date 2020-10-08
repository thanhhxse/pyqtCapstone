# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(525, 386)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setObjectName("image_label")
        self.verticalLayout.addWidget(self.image_label)
        self.control_bt = QtWidgets.QPushButton(Form)
        self.control_bt.setObjectName("control_bt")
        self.verticalLayout.addWidget(self.control_bt)
        self.horizontalLayout.addLayout(self.verticalLayout)
        #set slider

        
        self.sliderLayout = QtWidgets.QVBoxLayout()
        self.sliderLayout.setObjectName("sliderLayout")
        self.slider = QtWidgets.QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.changedValue)
        self.slider.setObjectName("slider_bar")
        self.label = QtWidgets.QLabel("0")
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        self.sliderLayout.addWidget(self.label)
        self.sliderLayout.addWidget(self.slider)
        self.horizontalLayout.addLayout(self.sliderLayout)

        # #slider
        # self.slider = QSlider()
        # self.slider.setOrientation(Qt.Horizontal)
        # self.slider.setTickPosition(QSlider.TicksBelow)
        # self.slider.setTickInterval(1)
        # self.slider.setMinimum(0)
        # self.slider.setMaximum(100)
        # self.slider.valueChanged.connect(self.changedValue)
        # self.label = QLabel("0")
        # self.label.setFont(QtGui.QFont("Sanserif", 15))
        # self.verticalLayout.addWidget(self.slider)
        # self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cam view"))
        self.image_label.setText(_translate("Form", "TextLabel"))
        self.control_bt.setText(_translate("Form", "Start"))


    def changedValue(self):
        size = self.slider.value()
        self.label.setText(str(size))
        
