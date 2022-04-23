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
        CDialog.resize(315, 142)
        self.gridLayout = QtWidgets.QGridLayout(CDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_gif = QtWidgets.QLabel(CDialog)
        self.label_gif.setObjectName("label_gif")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_gif)
        self.lineEdit = QtWidgets.QLineEdit(CDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_gif_3 = QtWidgets.QLabel(CDialog)
        self.label_gif_3.setObjectName("label_gif_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_gif_3)
        self.cbRole = QtWidgets.QComboBox(CDialog)
        self.cbRole.setObjectName("cbRole")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cbRole)
        self.label_gif_2 = QtWidgets.QLabel(CDialog)
        self.label_gif_2.setObjectName("label_gif_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_gif_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(CDialog)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.btnPopup = QtWidgets.QPushButton(CDialog)
        self.btnPopup.setObjectName("btnPopup")
        self.gridLayout.addWidget(self.btnPopup, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(CDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(CDialog)
        QtCore.QMetaObject.connectSlotsByName(CDialog)

    def retranslateUi(self, CDialog):
        _translate = QtCore.QCoreApplication.translate
        CDialog.setWindowTitle(_translate("CDialog", "Dialog"))
        self.label_gif.setText(_translate("CDialog", "姓名"))
        self.label_gif_3.setText(_translate("CDialog", "角色"))
        self.label_gif_2.setText(_translate("CDialog", "密码"))
        self.btnPopup.setText(_translate("CDialog", "popup"))

