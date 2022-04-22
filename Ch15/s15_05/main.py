#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.01.28   18:54
-------------------------------------------------------------------------------
   @Change:   2022.01.28
-------------------------------------------------------------------------------
"""

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QDialog

from Ch15.s15_05.dialog_a import Ui_CDialogA
from Ch15.s15_05.dialog_b import Ui_CDialogB
from Utils.Paths import ICON_PATH


class CDialogA(QDialog, Ui_CDialogA):
    def __init__(self, parent=None):
        super(CDialogA, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(ICON_PATH))
        self.btnDialogB.clicked.connect(self.slot_invokeDialogB)
        self.btnExit.clicked.connect(self.close)

    def slot_invokeDialogB(self):
        sender = self.sender()
        print(sender.text() + '按下')
        dialogB = CDialogB()
        dialogB.exec()


class CDialogB(QDialog, Ui_CDialogB):
    def __init__(self, parent=None):
        super(CDialogB, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(ICON_PATH))
        self.btnExit.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CDialogA()
    widget.show()
    sys.exit(app.exec_())
