# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CWidgetTask(object):
    def setupUi(self, CWidgetTask):
        CWidgetTask.setObjectName("CWidgetTask")
        CWidgetTask.resize(508, 116)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CWidgetTask.sizePolicy().hasHeightForWidth())
        CWidgetTask.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(CWidgetTask)
        self.gridLayout.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.leEstimatedWorkload = QtWidgets.QLineEdit(CWidgetTask)
        self.leEstimatedWorkload.setMaximumSize(QtCore.QSize(40, 16777215))
        self.leEstimatedWorkload.setObjectName("leEstimatedWorkload")
        self.gridLayout_2.addWidget(self.leEstimatedWorkload, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(CWidgetTask)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.labelTask = QtWidgets.QLabel(CWidgetTask)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTask.sizePolicy().hasHeightForWidth())
        self.labelTask.setSizePolicy(sizePolicy)
        self.labelTask.setObjectName("labelTask")
        self.gridLayout_2.addWidget(self.labelTask, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelDeveloper = QtWidgets.QLabel(CWidgetTask)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDeveloper.sizePolicy().hasHeightForWidth())
        self.labelDeveloper.setSizePolicy(sizePolicy)
        self.labelDeveloper.setMinimumSize(QtCore.QSize(50, 50))
        self.labelDeveloper.setMaximumSize(QtCore.QSize(50, 50))
        self.labelDeveloper.setFrameShape(QtWidgets.QFrame.Box)
        self.labelDeveloper.setText("")
        self.labelDeveloper.setObjectName("labelDeveloper")
        self.horizontalLayout_2.addWidget(self.labelDeveloper)
        self.pleTask = QtWidgets.QPlainTextEdit(CWidgetTask)
        self.pleTask.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pleTask.setObjectName("pleTask")
        self.horizontalLayout_2.addWidget(self.pleTask)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAccept = QtWidgets.QPushButton(CWidgetTask)
        self.btnAccept.setStyleSheet("QPushButton{\n"
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
        self.btnAccept.setObjectName("btnAccept")
        self.verticalLayout.addWidget(self.btnAccept)
        self.btnSave = QtWidgets.QPushButton(CWidgetTask)
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
        self.btnSave.setObjectName("btnSave")
        self.verticalLayout.addWidget(self.btnSave)
        self.btnFinished = QtWidgets.QPushButton(CWidgetTask)
        self.btnFinished.setStyleSheet("QPushButton{\n"
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
        self.btnFinished.setObjectName("btnFinished")
        self.verticalLayout.addWidget(self.btnFinished)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.retranslateUi(CWidgetTask)
        QtCore.QMetaObject.connectSlotsByName(CWidgetTask)

    def retranslateUi(self, CWidgetTask):
        _translate = QtCore.QCoreApplication.translate
        CWidgetTask.setWindowTitle(_translate("CWidgetTask", "Form"))
        self.label_2.setText(_translate("CWidgetTask", "estimated workload(man-day)"))
        self.labelTask.setText(_translate("CWidgetTask", "task"))
        self.btnAccept.setText(_translate("CWidgetTask", "sign on"))
        self.btnSave.setText(_translate("CWidgetTask", "save"))
        self.btnFinished.setText(_translate("CWidgetTask", "finished"))

