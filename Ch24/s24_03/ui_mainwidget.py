# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CMainWidget(object):
    def setupUi(self, CMainWidget):
        CMainWidget.setObjectName("CMainWidget")
        CMainWidget.resize(604, 397)
        CMainWidget.setStyleSheet("background-color: rgb(17, 149, 189);")
        self.verticalLayout = QtWidgets.QVBoxLayout(CMainWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnLogin = QtWidgets.QPushButton(CMainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLogin.sizePolicy().hasHeightForWidth())
        self.btnLogin.setSizePolicy(sizePolicy)
        self.btnLogin.setMinimumSize(QtCore.QSize(50, 50))
        self.btnLogin.setMaximumSize(QtCore.QSize(50, 50))
        self.btnLogin.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLogin.setIcon(icon)
        self.btnLogin.setIconSize(QtCore.QSize(40, 40))
        self.btnLogin.setObjectName("btnLogin")
        self.horizontalLayout_2.addWidget(self.btnLogin)
        self.btnMenu = QtWidgets.QPushButton(CMainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMenu.sizePolicy().hasHeightForWidth())
        self.btnMenu.setSizePolicy(sizePolicy)
        self.btnMenu.setMinimumSize(QtCore.QSize(50, 50))
        self.btnMenu.setMaximumSize(QtCore.QSize(50, 50))
        self.btnMenu.setStyleSheet("image: url(:/images/menu.png);")
        self.btnMenu.setText("")
        self.btnMenu.setIconSize(QtCore.QSize(40, 40))
        self.btnMenu.setFlat(False)
        self.btnMenu.setObjectName("btnMenu")
        self.horizontalLayout_2.addWidget(self.btnMenu)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.widget = QtWidgets.QWidget(CMainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(CMainWidget)
        QtCore.QMetaObject.connectSlotsByName(CMainWidget)

    def retranslateUi(self, CMainWidget):
        _translate = QtCore.QCoreApplication.translate
        CMainWidget.setWindowTitle(_translate("CMainWidget", "Form"))

import ks24_03_rc
