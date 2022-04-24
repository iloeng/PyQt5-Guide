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
        CDialog.resize(625, 389)
        self.gridLayout = QtWidgets.QGridLayout(CDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.movieLabel = QtWidgets.QLabel(CDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.movieLabel.sizePolicy().hasHeightForWidth())
        self.movieLabel.setSizePolicy(sizePolicy)
        self.movieLabel.setAutoFillBackground(True)
        self.movieLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.movieLabel.setObjectName("movieLabel")
        self.gridLayout.addWidget(self.movieLabel, 0, 0, 1, 1)
        self.frameSlider = QtWidgets.QSlider(CDialog)
        self.frameSlider.setOrientation(QtCore.Qt.Horizontal)
        self.frameSlider.setObjectName("frameSlider")
        self.gridLayout.addWidget(self.frameSlider, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openButton = QtWidgets.QToolButton(CDialog)
        self.openButton.setIconSize(QtCore.QSize(36, 36))
        self.openButton.setObjectName("openButton")
        self.horizontalLayout.addWidget(self.openButton)
        self.pauseButton = QtWidgets.QToolButton(CDialog)
        self.pauseButton.setIconSize(QtCore.QSize(36, 36))
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout.addWidget(self.pauseButton)
        self.stopButton = QtWidgets.QToolButton(CDialog)
        self.stopButton.setIconSize(QtCore.QSize(36, 36))
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout.addWidget(self.stopButton)
        self.quitButton = QtWidgets.QToolButton(CDialog)
        self.quitButton.setIconSize(QtCore.QSize(36, 36))
        self.quitButton.setObjectName("quitButton")
        self.horizontalLayout.addWidget(self.quitButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(CDialog)
        QtCore.QMetaObject.connectSlotsByName(CDialog)

    def retranslateUi(self, CDialog):
        _translate = QtCore.QCoreApplication.translate
        CDialog.setWindowTitle(_translate("CDialog", "Dialog"))
        self.movieLabel.setText(_translate("CDialog", "TextLabel"))
        self.openButton.setText(_translate("CDialog", "..."))
        self.pauseButton.setText(_translate("CDialog", "..."))
        self.stopButton.setText(_translate("CDialog", "..."))
        self.quitButton.setText(_translate("CDialog", "..."))

import Ch15.s15_12.ks15_12_rc
