# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addsprint.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CWidgetAddSprint(object):
    def setupUi(self, CWidgetAddSprint):
        CWidgetAddSprint.setObjectName("CWidgetAddSprint")
        CWidgetAddSprint.resize(626, 509)
        CWidgetAddSprint.setStyleSheet("background-color: rgb(17, 149, 189);")
        self.gridLayout = QtWidgets.QGridLayout(CWidgetAddSprint)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(CWidgetAddSprint)
        self.label_8.setMinimumSize(QtCore.QSize(150, 30))
        self.label_8.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.leCurrentSprint = QtWidgets.QLineEdit(CWidgetAddSprint)
        self.leCurrentSprint.setMinimumSize(QtCore.QSize(0, 30))
        self.leCurrentSprint.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leCurrentSprint.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.leCurrentSprint.setObjectName("leCurrentSprint")
        self.horizontalLayout_3.addWidget(self.leCurrentSprint)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dtStart = QtWidgets.QDateEdit(CWidgetAddSprint)
        self.dtStart.setMinimumSize(QtCore.QSize(0, 30))
        self.dtStart.setMaximumSize(QtCore.QSize(120, 16777215))
        self.dtStart.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.dtStart.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 11, 1), QtCore.QTime(0, 0, 0)))
        self.dtStart.setObjectName("dtStart")
        self.horizontalLayout_2.addWidget(self.dtStart)
        self.label_3 = QtWidgets.QLabel(CWidgetAddSprint)
        self.label_3.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.dtEnd = QtWidgets.QDateEdit(CWidgetAddSprint)
        self.dtEnd.setMinimumSize(QtCore.QSize(0, 30))
        self.dtEnd.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.dtEnd.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 12, 31), QtCore.QTime(0, 0, 0)))
        self.dtEnd.setTime(QtCore.QTime(0, 0, 0))
        self.dtEnd.setObjectName("dtEnd")
        self.horizontalLayout_2.addWidget(self.dtEnd)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(CWidgetAddSprint)
        self.label_9.setMinimumSize(QtCore.QSize(150, 30))
        self.label_9.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 6, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.btnGetback = QtWidgets.QPushButton(CWidgetAddSprint)
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
        self.btnSave = QtWidgets.QPushButton(CWidgetAddSprint)
        self.btnSave.setMinimumSize(QtCore.QSize(80, 30))
        self.btnSave.setStyleSheet("QPushButton{\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSave.setIcon(icon)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 2)
        self.leEstimatedWorkload = QtWidgets.QLineEdit(CWidgetAddSprint)
        self.leEstimatedWorkload.setMinimumSize(QtCore.QSize(0, 30))
        self.leEstimatedWorkload.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leEstimatedWorkload.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.leEstimatedWorkload.setObjectName("leEstimatedWorkload")
        self.gridLayout.addWidget(self.leEstimatedWorkload, 4, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.leProjectCode = QtWidgets.QLineEdit(CWidgetAddSprint)
        self.leProjectCode.setMinimumSize(QtCore.QSize(0, 30))
        self.leProjectCode.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.leProjectCode.setText("")
        self.leProjectCode.setReadOnly(False)
        self.leProjectCode.setObjectName("leProjectCode")
        self.horizontalLayout_4.addWidget(self.leProjectCode)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(CWidgetAddSprint)
        self.label_7.setMinimumSize(QtCore.QSize(150, 30))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(CWidgetAddSprint)
        self.label_15.setMinimumSize(QtCore.QSize(150, 30))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_15.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"border:none")
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(CWidgetAddSprint)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setStyleSheet("background-color: lightgray;\n"
"border-radius:5px;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.retranslateUi(CWidgetAddSprint)
        QtCore.QMetaObject.connectSlotsByName(CWidgetAddSprint)
        CWidgetAddSprint.setTabOrder(self.leProjectCode, self.leCurrentSprint)
        CWidgetAddSprint.setTabOrder(self.leCurrentSprint, self.dtStart)
        CWidgetAddSprint.setTabOrder(self.dtStart, self.dtEnd)
        CWidgetAddSprint.setTabOrder(self.dtEnd, self.leEstimatedWorkload)
        CWidgetAddSprint.setTabOrder(self.leEstimatedWorkload, self.btnGetback)
        CWidgetAddSprint.setTabOrder(self.btnGetback, self.btnSave)

    def retranslateUi(self, CWidgetAddSprint):
        _translate = QtCore.QCoreApplication.translate
        CWidgetAddSprint.setWindowTitle(_translate("CWidgetAddSprint", "add sprint"))
        self.label_8.setText(_translate("CWidgetAddSprint", "start date and end date"))
        self.leCurrentSprint.setText(_translate("CWidgetAddSprint", "2"))
        self.label_3.setText(_translate("CWidgetAddSprint", "-"))
        self.label_9.setText(_translate("CWidgetAddSprint", "estimated workload(man-day)"))
        self.btnGetback.setText(_translate("CWidgetAddSprint", "return"))
        self.btnSave.setText(_translate("CWidgetAddSprint", "save"))
        self.leEstimatedWorkload.setText(_translate("CWidgetAddSprint", "1"))
        self.label_7.setText(_translate("CWidgetAddSprint", "project code"))
        self.label_15.setText(_translate("CWidgetAddSprint", "sprint id"))
        self.label.setText(_translate("CWidgetAddSprint", "add sprint"))

import ks24_03_rc
