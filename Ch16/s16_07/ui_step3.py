# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'step3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CStep3(object):
    def setupUi(self, CStep3):
        CStep3.setObjectName("CStep3")
        CStep3.resize(353, 186)
        self.gridLayout = QtWidgets.QGridLayout(CStep3)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(CStep3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.btnPrevious = QtWidgets.QPushButton(CStep3)
        self.btnPrevious.setObjectName("btnPrevious")
        self.gridLayout.addWidget(self.btnPrevious, 1, 1, 1, 1)
        self.btnClose = QtWidgets.QPushButton(CStep3)
        self.btnClose.setObjectName("btnClose")
        self.gridLayout.addWidget(self.btnClose, 1, 2, 1, 1)

        self.retranslateUi(CStep3)
        QtCore.QMetaObject.connectSlotsByName(CStep3)

    def retranslateUi(self, CStep3):
        _translate = QtCore.QCoreApplication.translate
        CStep3.setWindowTitle(_translate("CStep3", "把大象装到冰箱里"))
        self.label.setText(_translate("CStep3", "第三步：把冰箱门带上。"))
        self.btnPrevious.setText(_translate("CStep3", "上一步"))
        self.btnClose.setText(_translate("CStep3", "关闭"))

