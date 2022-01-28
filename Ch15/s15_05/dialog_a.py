# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_a.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CDialogA(object):
    def setupUi(self, CDialogA):
        CDialogA.setObjectName("CDialogA")
        CDialogA.resize(215, 119)
        self.gridLayout = QtWidgets.QGridLayout(CDialogA)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(CDialogA)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.btnDialogB = QtWidgets.QPushButton(CDialogA)
        self.btnDialogB.setObjectName("btnDialogB")
        self.gridLayout.addWidget(self.btnDialogB, 1, 0, 1, 1)
        self.btnExit = QtWidgets.QPushButton(CDialogA)
        self.btnExit.setObjectName("btnExit")
        self.gridLayout.addWidget(self.btnExit, 1, 1, 1, 1)

        self.retranslateUi(CDialogA)
        QtCore.QMetaObject.connectSlotsByName(CDialogA)

    def retranslateUi(self, CDialogA):
        _translate = QtCore.QCoreApplication.translate
        CDialogA.setWindowTitle(_translate("CDialogA", "DialogA"))
        self.label.setText(_translate("CDialogA", "THIS IS DIALOG A!"))
        self.btnDialogB.setText(_translate("CDialogA", "dialog_b"))
        self.btnExit.setText(_translate("CDialogA", "exit"))

