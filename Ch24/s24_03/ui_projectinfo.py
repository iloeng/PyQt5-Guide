# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectinfo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CProjectInfo(object):
    def setupUi(self, CProjectInfo):
        CProjectInfo.setObjectName("CProjectInfo")
        CProjectInfo.resize(635, 511)
        CProjectInfo.setStyleSheet("background-color: rgb(17, 149, 189);")
        self.gridLayout = QtWidgets.QGridLayout(CProjectInfo)
        self.gridLayout.setObjectName("gridLayout")
        self.leEstimatedWorkload = QtWidgets.QLineEdit(CProjectInfo)
        self.leEstimatedWorkload.setMinimumSize(QtCore.QSize(0, 30))
        self.leEstimatedWorkload.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leEstimatedWorkload.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.leEstimatedWorkload.setObjectName("leEstimatedWorkload")
        self.gridLayout.addWidget(self.leEstimatedWorkload, 5, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(CProjectInfo)
        self.label_10.setMinimumSize(QtCore.QSize(150, 30))
        self.label_10.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 1)
        self.cbProductOwner = QtWidgets.QComboBox(CProjectInfo)
        self.cbProductOwner.setMinimumSize(QtCore.QSize(0, 30))
        self.cbProductOwner.setMaximumSize(QtCore.QSize(150, 16777215))
        self.cbProductOwner.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.cbProductOwner.setObjectName("cbProductOwner")
        self.gridLayout.addWidget(self.cbProductOwner, 6, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(CProjectInfo)
        self.label_8.setMinimumSize(QtCore.QSize(150, 30))
        self.label_8.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(CProjectInfo)
        self.label_9.setMinimumSize(QtCore.QSize(150, 30))
        self.label_9.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dtStart = QtWidgets.QDateEdit(CProjectInfo)
        self.dtStart.setMinimumSize(QtCore.QSize(0, 30))
        self.dtStart.setMaximumSize(QtCore.QSize(120, 16777215))
        self.dtStart.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.dtStart.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 11, 1), QtCore.QTime(0, 0, 0)))
        self.dtStart.setObjectName("dtStart")
        self.horizontalLayout_2.addWidget(self.dtStart)
        self.label_3 = QtWidgets.QLabel(CProjectInfo)
        self.label_3.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.dtEnd = QtWidgets.QDateEdit(CProjectInfo)
        self.dtEnd.setMinimumSize(QtCore.QSize(0, 30))
        self.dtEnd.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.dtEnd.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 12, 31), QtCore.QTime(0, 0, 0)))
        self.dtEnd.setTime(QtCore.QTime(0, 0, 0))
        self.dtEnd.setObjectName("dtEnd")
        self.horizontalLayout_2.addWidget(self.dtEnd)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.leCurrentSprint = QtWidgets.QLineEdit(CProjectInfo)
        self.leCurrentSprint.setMinimumSize(QtCore.QSize(0, 30))
        self.leCurrentSprint.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leCurrentSprint.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.leCurrentSprint.setObjectName("leCurrentSprint")
        self.gridLayout.addWidget(self.leCurrentSprint, 4, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(CProjectInfo)
        self.label_16.setMinimumSize(QtCore.QSize(150, 30))
        self.label_16.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 5, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(CProjectInfo)
        self.label_13.setMinimumSize(QtCore.QSize(150, 30))
        self.label_13.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_13.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 10, 0, 1, 1)
        self.leDevelopTeam = QtWidgets.QLineEdit(CProjectInfo)
        self.leDevelopTeam.setMinimumSize(QtCore.QSize(0, 30))
        self.leDevelopTeam.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.leDevelopTeam.setObjectName("leDevelopTeam")
        self.gridLayout.addWidget(self.leDevelopTeam, 10, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(CProjectInfo)
        self.label_11.setMinimumSize(QtCore.QSize(150, 30))
        self.label_11.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 7, 0, 1, 1)
        self.cbTest = QtWidgets.QComboBox(CProjectInfo)
        self.cbTest.setMinimumSize(QtCore.QSize(0, 30))
        self.cbTest.setMaximumSize(QtCore.QSize(150, 16777215))
        self.cbTest.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.cbTest.setObjectName("cbTest")
        self.gridLayout.addWidget(self.cbTest, 8, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(CProjectInfo)
        self.label_12.setMinimumSize(QtCore.QSize(150, 30))
        self.label_12.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 9, 0, 1, 1)
        self.cbScrumMaster = QtWidgets.QComboBox(CProjectInfo)
        self.cbScrumMaster.setMinimumSize(QtCore.QSize(0, 30))
        self.cbScrumMaster.setMaximumSize(QtCore.QSize(150, 16777215))
        self.cbScrumMaster.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.cbScrumMaster.setObjectName("cbScrumMaster")
        self.gridLayout.addWidget(self.cbScrumMaster, 7, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(CProjectInfo)
        self.label_14.setMinimumSize(QtCore.QSize(150, 30))
        self.label_14.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_14.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 8, 0, 1, 1)
        self.spinBoxSprintCycle = QtWidgets.QSpinBox(CProjectInfo)
        self.spinBoxSprintCycle.setMinimumSize(QtCore.QSize(0, 30))
        self.spinBoxSprintCycle.setMaximumSize(QtCore.QSize(150, 16777215))
        self.spinBoxSprintCycle.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.spinBoxSprintCycle.setMinimum(1)
        self.spinBoxSprintCycle.setMaximum(4)
        self.spinBoxSprintCycle.setProperty("value", 2)
        self.spinBoxSprintCycle.setObjectName("spinBoxSprintCycle")
        self.gridLayout.addWidget(self.spinBoxSprintCycle, 9, 1, 1, 1)
        self.leProjectCode = QtWidgets.QLineEdit(CProjectInfo)
        self.leProjectCode.setMinimumSize(QtCore.QSize(0, 30))
        self.leProjectCode.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.leProjectCode.setObjectName("leProjectCode")
        self.gridLayout.addWidget(self.leProjectCode, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(CProjectInfo)
        self.label_7.setMinimumSize(QtCore.QSize(150, 30))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(CProjectInfo)
        self.label_15.setMinimumSize(QtCore.QSize(150, 30))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_15.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"border:none")
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)
        self.leProjectName = QtWidgets.QLineEdit(CProjectInfo)
        self.leProjectName.setMinimumSize(QtCore.QSize(0, 30))
        self.leProjectName.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.leProjectName.setObjectName("leProjectName")
        self.gridLayout.addWidget(self.leProjectName, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 12, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btnGetback = QtWidgets.QPushButton(CProjectInfo)
        self.btnGetback.setMinimumSize(QtCore.QSize(100, 30))
        self.btnGetback.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border-radius:5px;")
        self.btnGetback.setObjectName("btnGetback")
        self.horizontalLayout.addWidget(self.btnGetback)
        self.btnSave = QtWidgets.QPushButton(CProjectInfo)
        self.btnSave.setMinimumSize(QtCore.QSize(80, 30))
        self.btnSave.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border-radius:5px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSave.setIcon(icon)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.gridLayout.addLayout(self.horizontalLayout, 11, 0, 1, 2)
        self.label = QtWidgets.QLabel(CProjectInfo)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setStyleSheet("background-color: lightgray;\n"
"border-radius:5px;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.retranslateUi(CProjectInfo)
        QtCore.QMetaObject.connectSlotsByName(CProjectInfo)
        CProjectInfo.setTabOrder(self.leProjectCode, self.leProjectName)
        CProjectInfo.setTabOrder(self.leProjectName, self.dtStart)
        CProjectInfo.setTabOrder(self.dtStart, self.dtEnd)
        CProjectInfo.setTabOrder(self.dtEnd, self.leCurrentSprint)
        CProjectInfo.setTabOrder(self.leCurrentSprint, self.leEstimatedWorkload)
        CProjectInfo.setTabOrder(self.leEstimatedWorkload, self.cbProductOwner)
        CProjectInfo.setTabOrder(self.cbProductOwner, self.cbScrumMaster)
        CProjectInfo.setTabOrder(self.cbScrumMaster, self.cbTest)
        CProjectInfo.setTabOrder(self.cbTest, self.spinBoxSprintCycle)
        CProjectInfo.setTabOrder(self.spinBoxSprintCycle, self.leDevelopTeam)
        CProjectInfo.setTabOrder(self.leDevelopTeam, self.btnGetback)
        CProjectInfo.setTabOrder(self.btnGetback, self.btnSave)

    def retranslateUi(self, CProjectInfo):
        _translate = QtCore.QCoreApplication.translate
        CProjectInfo.setWindowTitle(_translate("CProjectInfo", "Form"))
        self.leEstimatedWorkload.setText(_translate("CProjectInfo", "1000"))
        self.label_10.setText(_translate("CProjectInfo", "product owner"))
        self.label_8.setText(_translate("CProjectInfo", "start date and end date"))
        self.label_9.setText(_translate("CProjectInfo", "current sprint"))
        self.label_3.setText(_translate("CProjectInfo", "-"))
        self.leCurrentSprint.setText(_translate("CProjectInfo", "1"))
        self.label_16.setText(_translate("CProjectInfo", "estimated workload(man-day)"))
        self.label_13.setText(_translate("CProjectInfo", "develop team(Space as interval)"))
        self.label_11.setText(_translate("CProjectInfo", "SM"))
        self.label_12.setText(_translate("CProjectInfo", "sprint cycle(weeks)"))
        self.label_14.setText(_translate("CProjectInfo", "tester"))
        self.leProjectCode.setText(_translate("CProjectInfo", "JYF-QT5"))
        self.label_7.setText(_translate("CProjectInfo", "project code"))
        self.label_15.setText(_translate("CProjectInfo", "project name"))
        self.leProjectName.setText(_translate("CProjectInfo", "QT5实战指南"))
        self.btnGetback.setText(_translate("CProjectInfo", "return"))
        self.btnSave.setText(_translate("CProjectInfo", "save"))
        self.label.setText(_translate("CProjectInfo", "project info"))

import ks24_03_rc
