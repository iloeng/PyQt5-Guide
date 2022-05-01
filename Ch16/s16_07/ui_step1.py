# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'step1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CStep1(object):
    def setupUi(self, CStep1):
        CStep1.setObjectName("CStep1")
        CStep1.resize(353, 186)
        self.gridLayout = QtWidgets.QGridLayout(CStep1)
        self.gridLayout.setObjectName("gridLayout")
        self.btnNext = QtWidgets.QPushButton(CStep1)
        self.btnNext.setObjectName("btnNext")
        self.gridLayout.addWidget(self.btnNext, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(CStep1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.retranslateUi(CStep1)
        QtCore.QMetaObject.connectSlotsByName(CStep1)

    def retranslateUi(self, CStep1):
        _translate = QtCore.QCoreApplication.translate
        CStep1.setWindowTitle(_translate("CStep1", "把大象装到冰箱里"))
        self.btnNext.setText(_translate("CStep1", "下一步"))
        self.label.setText(_translate("CStep1", "第一步：打开冰箱门。"))

