# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_b.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CDialogB(object):
    def setupUi(self, CDialogB):
        CDialogB.setObjectName("CDialogB")
        CDialogB.resize(158, 131)
        self.verticalLayout = QtWidgets.QVBoxLayout(CDialogB)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(CDialogB)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.btnExit = QtWidgets.QPushButton(CDialogB)
        self.btnExit.setObjectName("btnExit")
        self.verticalLayout.addWidget(self.btnExit)

        self.retranslateUi(CDialogB)
        QtCore.QMetaObject.connectSlotsByName(CDialogB)

    def retranslateUi(self, CDialogB):
        _translate = QtCore.QCoreApplication.translate
        CDialogB.setWindowTitle(_translate("CDialogB", "DialogB"))
        self.label.setText(_translate("CDialogB", "DIALOG B!"))
        self.btnExit.setText(_translate("CDialogB", "exit"))

