# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CWidgetUser(object):
    def setupUi(self, CWidgetUser):
        CWidgetUser.setObjectName("CWidgetUser")
        CWidgetUser.resize(763, 549)
        CWidgetUser.setStyleSheet("background-color: rgb(17, 149, 189);")
        self.gridLayout_2 = QtWidgets.QGridLayout(CWidgetUser)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(223, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(17, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(CWidgetUser)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setStyleSheet("background-color: lightgray;\n"
"border-radius:5px;")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setMinimumSize(QtCore.QSize(100, 30))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"border:none")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.lePassword = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lePassword.sizePolicy().hasHeightForWidth())
        self.lePassword.setSizePolicy(sizePolicy)
        self.lePassword.setMinimumSize(QtCore.QSize(0, 30))
        self.lePassword.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lePassword.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lePassword.setObjectName("lePassword")
        self.gridLayout_3.addWidget(self.lePassword, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setMinimumSize(QtCore.QSize(100, 30))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setMinimumSize(QtCore.QSize(100, 30))
        self.label_13.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)
        self.leName = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leName.sizePolicy().hasHeightForWidth())
        self.leName.setSizePolicy(sizePolicy)
        self.leName.setMinimumSize(QtCore.QSize(0, 30))
        self.leName.setMaximumSize(QtCore.QSize(200, 16777215))
        self.leName.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.leName.setObjectName("leName")
        self.gridLayout_3.addWidget(self.leName, 1, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_photo = QtWidgets.QLabel(self.groupBox)
        self.label_photo.setMinimumSize(QtCore.QSize(100, 100))
        self.label_photo.setMaximumSize(QtCore.QSize(100, 100))
        self.label_photo.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_photo.setText("")
        self.label_photo.setObjectName("label_photo")
        self.verticalLayout.addWidget(self.label_photo)
        self.btnSelectPhoto = QtWidgets.QToolButton(self.groupBox)
        self.btnSelectPhoto.setObjectName("btnSelectPhoto")
        self.verticalLayout.addWidget(self.btnSelectPhoto)
        self.gridLayout_3.addLayout(self.verticalLayout, 3, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setMinimumSize(QtCore.QSize(100, 30))
        self.label_12.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 3, 0, 1, 1)
        self.leId = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leId.sizePolicy().hasHeightForWidth())
        self.leId.setSizePolicy(sizePolicy)
        self.leId.setMinimumSize(QtCore.QSize(0, 30))
        self.leId.setMaximumSize(QtCore.QSize(200, 16777215))
        self.leId.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.leId.setReadOnly(True)
        self.leId.setObjectName("leId")
        self.gridLayout_3.addWidget(self.leId, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(141, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.btnGetback = QtWidgets.QPushButton(self.groupBox)
        self.btnGetback.setMinimumSize(QtCore.QSize(100, 30))
        self.btnGetback.setStyleSheet("QPushButton{\n"
"border:1px solid black;\n"
"border-radius:4px;\n"
"padding:4px;\n"
"}\n"
"QPushButton::hover{\n"
"border:1px solid black;\n"
"border-radius:4px;\n"
"background-color:lightgray;\n"
"padding:4px\n"
"}\n"
"QPushButton::pressed{\n"
"border:1px solid black;\n"
"border-radius:4px;\n"
"background-color:gray;\n"
"padding:4px\n"
"}")
        self.btnGetback.setObjectName("btnGetback")
        self.horizontalLayout.addWidget(self.btnGetback)
        self.btnSave = QtWidgets.QPushButton(self.groupBox)
        self.btnSave.setMinimumSize(QtCore.QSize(100, 30))
        self.btnSave.setStyleSheet("QPushButton{\n"
"border:1px solid black;\n"
"border-radius:4px;\n"
"padding:4px;\n"
"}\n"
"QPushButton::hover{\n"
"border:1px solid black;\n"
"border-radius:4px;\n"
"background-color:lightgray;\n"
"padding:4px\n"
"}\n"
"QPushButton::pressed{\n"
"border:1px solid black;\n"
"border-radius:4px;\n"
"background-color:gray;\n"
"padding:4px\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSave.setIcon(icon)
        self.btnSave.setDefault(False)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 1, 1)

        self.retranslateUi(CWidgetUser)
        QtCore.QMetaObject.connectSlotsByName(CWidgetUser)
        CWidgetUser.setTabOrder(self.leId, self.leName)
        CWidgetUser.setTabOrder(self.leName, self.lePassword)
        CWidgetUser.setTabOrder(self.lePassword, self.btnSelectPhoto)
        CWidgetUser.setTabOrder(self.btnSelectPhoto, self.btnGetback)
        CWidgetUser.setTabOrder(self.btnGetback, self.btnSave)

    def retranslateUi(self, CWidgetUser):
        _translate = QtCore.QCoreApplication.translate
        CWidgetUser.setWindowTitle(_translate("CWidgetUser", "Form"))
        self.label.setText(_translate("CWidgetUser", "user"))
        self.label_7.setText(_translate("CWidgetUser", "name"))
        self.label_9.setText(_translate("CWidgetUser", "password"))
        self.label_13.setText(_translate("CWidgetUser", "ID"))
        self.btnSelectPhoto.setText(_translate("CWidgetUser", "..."))
        self.label_12.setText(_translate("CWidgetUser", "photo"))
        self.btnGetback.setText(_translate("CWidgetUser", "return"))
        self.btnSave.setText(_translate("CWidgetUser", "save"))

import ks24_03_rc
