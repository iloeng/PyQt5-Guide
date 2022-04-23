#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.04.23   17:05
-------------------------------------------------------------------------------
   @Change:   2022.04.23
-------------------------------------------------------------------------------
"""
import sys

from enum import Enum
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

from Ch15.s15_10.ui_dialog import Ui_CDialog
from Utils.Paths import ICON_PATH


class CDialog(QDialog, Ui_CDialog):

    class EUserType(Enum):
        EUserType_Invalid = 0
        EUserType_Admin = 1
        EUserType_User = 2
        EUserType_Guest = 3
        EUserType_Other = 4
        EUserType_Max = 5

    def __init__(self, parent=None):
        super(CDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(ICON_PATH))

        # addItem 当前第 0 条
        self.cbRole.addItem('user', self.EUserType.EUserType_User)
        # 当前第 1 条
        self.cbRole.addItem('guest')
        self.cbRole.setItemData(1, self.EUserType.EUserType_Guest)
        self.cbRole.addItem(QIcon(':/images/other.png'), 'other', self.EUserType.EUserType_Other)
        strList = ['maintain', 'security', 'other']
        self.cbRole.addItems(strList)
        # 在 user 之前插入一条记录， 将在第 0 条之前插入， 'admin' 将变成第 0 条
        self.cbRole.currentIndexChanged.connect(self.slot_cbRoleChanged)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.btnPopup.clicked.connect(self.slot_popup)

    def slot_popup(self):
        self.cbRole.currentText()

    def slot_cbRoleChanged(self, index):
        str = self.cbRole.currentText()
        eUserType = self.cbRole.itemData(index)
        if eUserType == self.EUserType.EUserType_Admin:
            strInfo = str + ','
            str = f'idx = {index}, usertype enum value = {eUserType}'
            strInfo += str
            print(strInfo)
            QMessageBox.information(self, 'ComboBox selection change', strInfo)
        else:
            strInfo = str + ','
            str = f'idx:{index}, usertype enum value:{eUserType}'
            strInfo += str
            print(strInfo)
            QMessageBox.information(self, 'ComboBox selection change', strInfo)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CDialog()
    widget.show()
    sys.exit(app.exec_())
