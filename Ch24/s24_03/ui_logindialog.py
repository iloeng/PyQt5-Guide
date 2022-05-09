# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logindialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CLoginDialog(object):
    def setupUi(self, CLoginDialog):
        CLoginDialog.setObjectName("CLoginDialog")
        CLoginDialog.resize(281, 106)
        self.gridLayout = QtWidgets.QGridLayout(CLoginDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_gif = QtWidgets.QLabel(CLoginDialog)
        self.label_gif.setObjectName("label_gif")
        self.gridLayout.addWidget(self.label_gif, 0, 0, 1, 1)
        self.leName = QtWidgets.QLineEdit(CLoginDialog)
        self.leName.setObjectName("leName")
        self.gridLayout.addWidget(self.leName, 0, 1, 1, 1)
        self.lePassword = QtWidgets.QLineEdit(CLoginDialog)
        self.lePassword.setObjectName("lePassword")
        self.gridLayout.addWidget(self.lePassword, 1, 1, 1, 1)
        self.label_gif_2 = QtWidgets.QLabel(CLoginDialog)
        self.label_gif_2.setObjectName("label_gif_2")
        self.gridLayout.addWidget(self.label_gif_2, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(CLoginDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(CLoginDialog)
        QtCore.QMetaObject.connectSlotsByName(CLoginDialog)

    def retranslateUi(self, CLoginDialog):
        _translate = QtCore.QCoreApplication.translate
        CLoginDialog.setWindowTitle(_translate("CLoginDialog", "Dialog"))
        self.label_gif.setText(_translate("CLoginDialog", "user name"))
        self.label_gif_2.setText(_translate("CLoginDialog", "password"))

