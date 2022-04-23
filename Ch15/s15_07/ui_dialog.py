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
        CDialog.resize(349, 200)
        self.gridLayout = QtWidgets.QGridLayout(CDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.btnExit = QtWidgets.QPushButton(CDialog)
        self.btnExit.setObjectName("btnExit")
        self.gridLayout.addWidget(self.btnExit, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(CDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.placeHolderwidget = QtWidgets.QWidget(CDialog)
        self.placeHolderwidget.setObjectName("placeHolderwidget")
        self.gridLayout.addWidget(self.placeHolderwidget, 1, 0, 1, 2)

        self.retranslateUi(CDialog)
        QtCore.QMetaObject.connectSlotsByName(CDialog)

    def retranslateUi(self, CDialog):
        _translate = QtCore.QCoreApplication.translate
        CDialog.setWindowTitle(_translate("CDialog", "DialogA"))
        self.btnExit.setText(_translate("CDialog", "exit"))
        self.label.setText(_translate("CDialog", "THIS IS DIALOG!"))

