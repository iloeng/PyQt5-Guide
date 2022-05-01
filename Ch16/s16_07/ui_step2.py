# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'step2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CStep2(object):
    def setupUi(self, CStep2):
        CStep2.setObjectName("CStep2")
        CStep2.resize(353, 186)
        self.gridLayout = QtWidgets.QGridLayout(CStep2)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.btnPrevious = QtWidgets.QPushButton(CStep2)
        self.btnPrevious.setObjectName("btnPrevious")
        self.gridLayout.addWidget(self.btnPrevious, 1, 1, 1, 1)
        self.btnNext = QtWidgets.QPushButton(CStep2)
        self.btnNext.setObjectName("btnNext")
        self.gridLayout.addWidget(self.btnNext, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(CStep2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.retranslateUi(CStep2)
        QtCore.QMetaObject.connectSlotsByName(CStep2)

    def retranslateUi(self, CStep2):
        _translate = QtCore.QCoreApplication.translate
        CStep2.setWindowTitle(_translate("CStep2", "把大象装到冰箱里"))
        self.btnPrevious.setText(_translate("CStep2", "上一步"))
        self.btnNext.setText(_translate("CStep2", "下一步"))
        self.label.setText(_translate("CStep2", "第二步：把大象装进去。"))

