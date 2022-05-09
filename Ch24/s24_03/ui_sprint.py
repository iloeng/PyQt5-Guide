# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sprint.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CWidgetSprint(object):
    def setupUi(self, CWidgetSprint):
        CWidgetSprint.setObjectName("CWidgetSprint")
        CWidgetSprint.resize(945, 1115)
        CWidgetSprint.setStyleSheet("background-color: rgb(17, 149, 189);")
        self.gridLayout_4 = QtWidgets.QGridLayout(CWidgetSprint)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(CWidgetSprint)
        self.label.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 2)
        self.label_projectName = QtWidgets.QLabel(CWidgetSprint)
        self.label_projectName.setMinimumSize(QtCore.QSize(300, 30))
        self.label_projectName.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.label_projectName.setObjectName("label_projectName")
        self.gridLayout_4.addWidget(self.label_projectName, 1, 0, 1, 1)
        self.label_sprintNo = QtWidgets.QLabel(CWidgetSprint)
        self.label_sprintNo.setMinimumSize(QtCore.QSize(100, 0))
        self.label_sprintNo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.label_sprintNo.setObjectName("label_sprintNo")
        self.gridLayout_4.addWidget(self.label_sprintNo, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAddBacklog = QtWidgets.QPushButton(CWidgetSprint)
        self.btnAddBacklog.setMinimumSize(QtCore.QSize(0, 60))
        self.btnAddBacklog.setAutoFillBackground(False)
        self.btnAddBacklog.setStyleSheet("QPushButton{\n"
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
        self.btnAddBacklog.setObjectName("btnAddBacklog")
        self.horizontalLayout.addWidget(self.btnAddBacklog)
        self.btnBurndown = QtWidgets.QPushButton(CWidgetSprint)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBurndown.sizePolicy().hasHeightForWidth())
        self.btnBurndown.setSizePolicy(sizePolicy)
        self.btnBurndown.setMinimumSize(QtCore.QSize(0, 60))
        self.btnBurndown.setStyleSheet("QPushButton{\n"
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
        icon.addPixmap(QtGui.QPixmap(":/images/burndown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBurndown.setIcon(icon)
        self.btnBurndown.setIconSize(QtCore.QSize(30, 30))
        self.btnBurndown.setObjectName("btnBurndown")
        self.horizontalLayout.addWidget(self.btnBurndown)
        self.btnFinish = QtWidgets.QPushButton(CWidgetSprint)
        self.btnFinish.setMinimumSize(QtCore.QSize(0, 60))
        self.btnFinish.setAutoFillBackground(False)
        self.btnFinish.setStyleSheet("QPushButton{\n"
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
        self.btnFinish.setObjectName("btnFinish")
        self.horizontalLayout.addWidget(self.btnFinish)
        self.btnGetback = QtWidgets.QPushButton(CWidgetSprint)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGetback.sizePolicy().hasHeightForWidth())
        self.btnGetback.setSizePolicy(sizePolicy)
        self.btnGetback.setMinimumSize(QtCore.QSize(80, 60))
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 0, 1, 4)
        self.scrollArea = QtWidgets.QScrollArea(CWidgetSprint)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 900, 941))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_5 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_7 = QtWidgets.QFrame(self.widget_5)
        self.frame_7.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_3.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_doing = QtWidgets.QLabel(self.frame_7)
        self.label_doing.setStyleSheet("background-color: rgb(205, 205, 205);\n"
"border-radius:5px;\n"
"border:none")
        self.label_doing.setAlignment(QtCore.Qt.AlignCenter)
        self.label_doing.setObjectName("label_doing")
        self.gridLayout_3.addWidget(self.label_doing, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_7, 0, 1, 1, 1)
        self.frame_10 = QtWidgets.QFrame(self.widget_5)
        self.frame_10.setStyleSheet("background-color: rgb(182, 182, 182);\n"
"border-top-right-radius:5px;\n"
"border-bottom-right-radius:5px;")
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_10.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_10.setSpacing(3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_finished = QtWidgets.QLabel(self.frame_10)
        self.label_finished.setStyleSheet("background-color: rgb(205, 205, 205);\n"
"border-radius:5px;\n"
"border:none")
        self.label_finished.setAlignment(QtCore.Qt.AlignCenter)
        self.label_finished.setObjectName("label_finished")
        self.gridLayout_10.addWidget(self.label_finished, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_10, 0, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.widget_5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)
        self.frame_2 = QtWidgets.QFrame(self.widget_5)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setStyleSheet("background-color: rgb(182, 182, 182);\n"
"border-top-left-radius:5px;\n"
"border-bottom-left-radius:5px;")
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_6.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_toDo = QtWidgets.QLabel(self.frame_2)
        self.label_toDo.setMinimumSize(QtCore.QSize(0, 30))
        self.label_toDo.setStyleSheet("background-color: rgb(205, 205, 205);\n"
"border-radius:5px;\n"
"border:none")
        self.label_toDo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_toDo.setObjectName("label_toDo")
        self.gridLayout_6.addWidget(self.label_toDo, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_5, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 917, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 3, 0, 1, 4)

        self.retranslateUi(CWidgetSprint)
        QtCore.QMetaObject.connectSlotsByName(CWidgetSprint)

    def retranslateUi(self, CWidgetSprint):
        _translate = QtCore.QCoreApplication.translate
        CWidgetSprint.setWindowTitle(_translate("CWidgetSprint", "Form"))
        self.label.setText(_translate("CWidgetSprint", "Sprint Info"))
        self.label_projectName.setText(_translate("CWidgetSprint", "项目名称"))
        self.label_sprintNo.setText(_translate("CWidgetSprint", "迭代1"))
        self.btnAddBacklog.setText(_translate("CWidgetSprint", "add Backlog"))
        self.btnBurndown.setText(_translate("CWidgetSprint", "burndown"))
        self.btnFinish.setText(_translate("CWidgetSprint", "all backlogs are done"))
        self.btnGetback.setText(_translate("CWidgetSprint", "return"))
        self.label_doing.setText(_translate("CWidgetSprint", "doing"))
        self.label_finished.setText(_translate("CWidgetSprint", "done"))
        self.label_toDo.setText(_translate("CWidgetSprint", "backlog"))

import ks24_03_rc
