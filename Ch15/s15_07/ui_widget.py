# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CWidget(object):
    def setupUi(self, CWidget):
        CWidget.setObjectName("CWidget")
        CWidget.resize(384, 205)
        CWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.gridLayout = QtWidgets.QGridLayout(CWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(CWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(CWidget)
        QtCore.QMetaObject.connectSlotsByName(CWidget)

    def retranslateUi(self, CWidget):
        _translate = QtCore.QCoreApplication.translate
        CWidget.setWindowTitle(_translate("CWidget", "Form"))
        self.label.setText(_translate("CWidget", "THIS IS WIDGET B！"))

