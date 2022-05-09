# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'burndown.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CWidgetBurndown(object):
    def setupUi(self, CWidgetBurndown):
        CWidgetBurndown.setObjectName("CWidgetBurndown")
        CWidgetBurndown.resize(763, 549)
        CWidgetBurndown.setStyleSheet("background-color: rgb(17, 149, 189);")
        self.gridLayout_2 = QtWidgets.QGridLayout(CWidgetBurndown)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(CWidgetBurndown)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(500, 500))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_projectName = QtWidgets.QLabel(self.groupBox)
        self.label_projectName.setMinimumSize(QtCore.QSize(0, 30))
        self.label_projectName.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_projectName.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.label_projectName.setObjectName("label_projectName")
        self.horizontalLayout_2.addWidget(self.label_projectName)
        self.label_sprintNo = QtWidgets.QLabel(self.groupBox)
        self.label_sprintNo.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_sprintNo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.label_sprintNo.setObjectName("label_sprintNo")
        self.horizontalLayout_2.addWidget(self.label_sprintNo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(100, 100))
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(141, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnGetback = QtWidgets.QPushButton(self.groupBox)
        self.btnGetback.setMinimumSize(QtCore.QSize(100, 30))
        self.btnGetback.setStyleSheet("QPushButton{\n"
"border:1px solid black;\n"
"border-radius:4px;\n"
"padding:4px;\n"
"}\n"
"QPushButton::hover{\n"
"border:1px solid black;\n"
"border-radius:4px;\n"
"background-color:lightgray;\n"
"padding:4px\n"
"}\n"
"QPushButton::pressed{\n"
"border:1px solid black;\n"
"border-radius:4px;\n"
"background-color:gray;\n"
"padding:4px\n"
"}")
        self.btnGetback.setObjectName("btnGetback")
        self.horizontalLayout.addWidget(self.btnGetback)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(223, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(17, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 2, 1, 1, 1)

        self.retranslateUi(CWidgetBurndown)
        QtCore.QMetaObject.connectSlotsByName(CWidgetBurndown)

    def retranslateUi(self, CWidgetBurndown):
        _translate = QtCore.QCoreApplication.translate
        CWidgetBurndown.setWindowTitle(_translate("CWidgetBurndown", "Form"))
        self.label_projectName.setText(_translate("CWidgetBurndown", "项目名称"))
        self.label_sprintNo.setText(_translate("CWidgetBurndown", "迭代1"))
        self.btnGetback.setText(_translate("CWidgetBurndown", "return"))

import ks24_03_rc
