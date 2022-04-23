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
        CDialog.resize(281, 106)
        self.gridLayout = QtWidgets.QGridLayout(CDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_gif = QtWidgets.QLabel(CDialog)
        self.label_gif.setObjectName("label_gif")
        self.gridLayout.addWidget(self.label_gif, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(CDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lePassword = QtWidgets.QLineEdit(CDialog)
        self.lePassword.setObjectName("lePassword")
        self.gridLayout.addWidget(self.lePassword, 1, 1, 1, 1)
        self.label_gif_2 = QtWidgets.QLabel(CDialog)
        self.label_gif_2.setObjectName("label_gif_2")
        self.gridLayout.addWidget(self.label_gif_2, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(CDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(CDialog)
        QtCore.QMetaObject.connectSlotsByName(CDialog)

    def retranslateUi(self, CDialog):
        _translate = QtCore.QCoreApplication.translate
        CDialog.setWindowTitle(_translate("CDialog", "Dialog"))
        self.label_gif.setText(_translate("CDialog", "姓名"))
        self.label_gif_2.setText(_translate("CDialog", "密码"))

