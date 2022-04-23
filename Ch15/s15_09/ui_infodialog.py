# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infodialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CInfoDialog(object):
    def setupUi(self, CInfoDialog):
        CInfoDialog.setObjectName("CInfoDialog")
        CInfoDialog.resize(268, 190)
        self.verticalLayout = QtWidgets.QVBoxLayout(CInfoDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ckEditable = QtWidgets.QCheckBox(CInfoDialog)
        self.ckEditable.setObjectName("ckEditable")
        self.verticalLayout.addWidget(self.ckEditable)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(CInfoDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.leName = QtWidgets.QLineEdit(CInfoDialog)
        self.leName.setEnabled(False)
        self.leName.setObjectName("leName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leName)
        self.label_2 = QtWidgets.QLabel(CInfoDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.leStature = QtWidgets.QLineEdit(CInfoDialog)
        self.leStature.setEnabled(False)
        self.leStature.setObjectName("leStature")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.leStature)
        self.birthday = QtWidgets.QLabel(CInfoDialog)
        self.birthday.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.birthday.setObjectName("birthday")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.birthday)
        self.address = QtWidgets.QLabel(CInfoDialog)
        self.address.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.address.setObjectName("address")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.address)
        self.lePhone = QtWidgets.QLineEdit(CInfoDialog)
        self.lePhone.setEnabled(False)
        self.lePhone.setObjectName("lePhone")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lePhone)
        self.leBirthday = QtWidgets.QLineEdit(CInfoDialog)
        self.leBirthday.setEnabled(False)
        self.leBirthday.setObjectName("leBirthday")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.leBirthday)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(CInfoDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CInfoDialog)
        QtCore.QMetaObject.connectSlotsByName(CInfoDialog)
        CInfoDialog.setTabOrder(self.ckEditable, self.leName)
        CInfoDialog.setTabOrder(self.leName, self.leStature)
        CInfoDialog.setTabOrder(self.leStature, self.leBirthday)
        CInfoDialog.setTabOrder(self.leBirthday, self.lePhone)

    def retranslateUi(self, CInfoDialog):
        _translate = QtCore.QCoreApplication.translate
        CInfoDialog.setWindowTitle(_translate("CInfoDialog", "Dialog"))
        self.ckEditable.setText(_translate("CInfoDialog", "允许编辑"))
        self.label.setText(_translate("CInfoDialog", "姓名"))
        self.label_2.setText(_translate("CInfoDialog", "身高"))
        self.birthday.setText(_translate("CInfoDialog", "生日"))
        self.address.setText(_translate("CInfoDialog", "电话"))

