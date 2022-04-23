#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.04.23   16:50
-------------------------------------------------------------------------------
   @Change:   2022.04.23
-------------------------------------------------------------------------------
"""

import sys

from PyQt5.QtGui import QIcon, QIntValidator, QRegExpValidator
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QRegExp

from Ch15.s15_09.ui_dialog import *
from Ch15.s15_09.ui_infodialog import *
from Utils.Paths import ICON_PATH


class CDialog(QDialog, Ui_CDialog):

    def __init__(self, parent=None):
        super(CDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(ICON_PATH))
        self.buttonBox.accepted.connect(self.slot_accept)
        self.buttonBox.rejected.connect(self.reject)
        # 设置密码的 echoMode
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lePassword.setPlaceholderText('Please Input Password.')

    def slot_accept(self):
        infodialog = CInfoDialog(self)
        infodialog.exec()


class CInfoDialog(QDialog, Ui_CInfoDialog):
    def __init__(self, parent=None):
        super(CInfoDialog, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.ckEditable.stateChanged.connect(self.slot_editEnabled)

        # setValidator for leStature
        self.leStature.setValidator(QIntValidator(0, 300, self.leStature))  # min:0cm, max:300cm
        # setMask for leBirthday, 年年年年-月月-日日
        self.leBirthday.setInputMask("0000-00-00")
        self.leBirthday.setText("00000000")
        self.leBirthday.setCursorPosition(0)

        # mask & validator,单纯使用mask无法约束数值的范围
        regExp = QRegExp("^1[3|4|5|8][0-9][0-9]{8}")
        self.lePhone.setValidator(QRegExpValidator(regExp, self.lePhone))
        self.lePhone.setInputMask("#00-000-00000000")  # eg. +86-135-87989898
        self.lePhone.setText("+00-000-00000000")

    def slot_editEnabled(self, b):
        self.leName.setEnabled(b)
        self.leStature.setEnabled(b)
        self.leBirthday.setEnabled(b)
        self.lePhone.setEnabled(b)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CDialog()
    widget.show()
    sys.exit(app.exec_())

