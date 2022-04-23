#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    vboxlayout.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.04.23   14:15
-------------------------------------------------------------------------------
   @Change:   2022.04.23
-------------------------------------------------------------------------------
"""

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QDialog

from Ch15.s15_06.ui_vboxlayout import Ui_DialogVBox
from Ch15.s15_06.ui_hboxlayout import Ui_DialogHBox
from Ch15.s15_06.ui_formlayout import Ui_DialogForm
from Ch15.s15_06.ui_gridlayout import Ui_DialogGrid

from Utils.Paths import ICON_PATH


class CDialogVBox(QDialog, Ui_DialogVBox):
    def __init__(self, parent=None):
        super(CDialogVBox, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(ICON_PATH))


class CDialogHBox(QDialog, Ui_DialogHBox):
    def __init__(self, parent=None):
        super(CDialogHBox, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(ICON_PATH))


class CDialogForm(QDialog, Ui_DialogForm):
    def __init__(self, parent=None):
        super(CDialogForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(ICON_PATH))


class CDialogGrid(QDialog, Ui_DialogGrid):
    def __init__(self, parent=None):
        super(CDialogGrid, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(ICON_PATH))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget1 = CDialogVBox()
    widget1.show()
    widget2 = CDialogHBox()
    widget2.show()
    widget3 = CDialogForm()
    widget3.show()
    widget4 = CDialogGrid()
    widget4.show()
    sys.exit(app.exec_())

