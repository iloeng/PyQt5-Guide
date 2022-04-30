# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maindialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CMainDialog(object):
    def setupUi(self, CMainDialog):
        CMainDialog.setObjectName("CMainDialog")
        CMainDialog.resize(383, 218)
        self.verticalLayout = QtWidgets.QVBoxLayout(CMainDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(CMainDialog)
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(CMainDialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(CMainDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_gif = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_gif.sizePolicy().hasHeightForWidth())
        self.label_gif.setSizePolicy(sizePolicy)
        self.label_gif.setObjectName("label_gif")
        self.gridLayout.addWidget(self.label_gif, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(CMainDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_png = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_png.sizePolicy().hasHeightForWidth())
        self.label_png.setSizePolicy(sizePolicy)
        self.label_png.setObjectName("label_png")
        self.gridLayout_2.addWidget(self.label_png, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(CMainDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CMainDialog)
        self.buttonBox.accepted.connect(CMainDialog.accept)
        self.buttonBox.rejected.connect(CMainDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CMainDialog)

    def retranslateUi(self, CMainDialog):
        _translate = QtCore.QCoreApplication.translate
        CMainDialog.setWindowTitle(_translate("CMainDialog", "Dialog"))
        self.pushButton.setText(_translate("CMainDialog", "start"))
        self.label.setText(_translate("CMainDialog", "TextLabel"))
        self.groupBox.setTitle(_translate("CMainDialog", "GroupBox"))
        self.label_gif.setText(_translate("CMainDialog", "TextLabel"))
        self.groupBox_2.setTitle(_translate("CMainDialog", "GroupBox"))
        self.label_png.setText(_translate("CMainDialog", "TextLabel"))

