# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CDialog(object):
    def setupUi(self, CDialog):
        CDialog.setObjectName("CDialog")
        CDialog.resize(584, 202)
        self.gridLayout = QtWidgets.QGridLayout(CDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(CDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/elephant.png"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.retranslateUi(CDialog)
        QtCore.QMetaObject.connectSlotsByName(CDialog)

    def retranslateUi(self, CDialog):
        _translate = QtCore.QCoreApplication.translate
        CDialog.setWindowTitle(_translate("CDialog", "Dialog"))

