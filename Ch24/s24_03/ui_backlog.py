# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backlog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CWidgetBacklog(object):
    def setupUi(self, CWidgetBacklog):
        CWidgetBacklog.setObjectName("CWidgetBacklog")
        CWidgetBacklog.resize(468, 182)
        CWidgetBacklog.setAutoFillBackground(True)
        self.gridLayout = QtWidgets.QGridLayout(CWidgetBacklog)
        self.gridLayout.setObjectName("gridLayout")
        self.labelBacklog = QtWidgets.QLabel(CWidgetBacklog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBacklog.sizePolicy().hasHeightForWidth())
        self.labelBacklog.setSizePolicy(sizePolicy)
        self.labelBacklog.setObjectName("labelBacklog")
        self.gridLayout.addWidget(self.labelBacklog, 0, 0, 1, 1)
        self.pleBacklog = QtWidgets.QPlainTextEdit(CWidgetBacklog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pleBacklog.sizePolicy().hasHeightForWidth())
        self.pleBacklog.setSizePolicy(sizePolicy)
        self.pleBacklog.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pleBacklog.setObjectName("pleBacklog")
        self.gridLayout.addWidget(self.pleBacklog, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 7, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(CWidgetBacklog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.leEstimatedWorkload = QtWidgets.QLineEdit(CWidgetBacklog)
        self.leEstimatedWorkload.setMaximumSize(QtCore.QSize(40, 16777215))
        self.leEstimatedWorkload.setObjectName("leEstimatedWorkload")
        self.horizontalLayout.addWidget(self.leEstimatedWorkload)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnSave = QtWidgets.QPushButton(CWidgetBacklog)
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
        self.btnSave.setFlat(False)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.btnAddTask = QtWidgets.QPushButton(CWidgetBacklog)
        self.btnAddTask.setStyleSheet("QPushButton{\n"
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
        self.btnAddTask.setObjectName("btnAddTask")
        self.horizontalLayout.addWidget(self.btnAddTask)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.frameTasks = QtWidgets.QFrame(CWidgetBacklog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameTasks.sizePolicy().hasHeightForWidth())
        self.frameTasks.setSizePolicy(sizePolicy)
        self.frameTasks.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTasks.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTasks.setObjectName("frameTasks")
        self.gridLayout.addWidget(self.frameTasks, 3, 0, 1, 1)

        self.retranslateUi(CWidgetBacklog)
        QtCore.QMetaObject.connectSlotsByName(CWidgetBacklog)

    def retranslateUi(self, CWidgetBacklog):
        _translate = QtCore.QCoreApplication.translate
        CWidgetBacklog.setWindowTitle(_translate("CWidgetBacklog", "Form"))
        self.labelBacklog.setText(_translate("CWidgetBacklog", "backlog"))
        self.label_2.setText(_translate("CWidgetBacklog", "estimated workload(man-day)"))
        self.btnSave.setText(_translate("CWidgetBacklog", "save"))
        self.btnAddTask.setText(_translate("CWidgetBacklog", "add task"))

