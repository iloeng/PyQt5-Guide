# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customwidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CCustomWidget(object):
    def setupUi(self, CCustomWidget):
        CCustomWidget.setObjectName("CCustomWidget")
        CCustomWidget.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(CCustomWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 30)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_gif = QtWidgets.QLabel(CCustomWidget)
        self.label_gif.setObjectName("label_gif")
        self.gridLayout.addWidget(self.label_gif, 0, 0, 1, 1)

        self.retranslateUi(CCustomWidget)
        QtCore.QMetaObject.connectSlotsByName(CCustomWidget)

    def retranslateUi(self, CCustomWidget):
        _translate = QtCore.QCoreApplication.translate
        CCustomWidget.setWindowTitle(_translate("CCustomWidget", "Form"))
        self.label_gif.setText(_translate("CCustomWidget", "TextLabel"))

