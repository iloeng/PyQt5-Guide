#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.01.28   15:02
-------------------------------------------------------------------------------
   @Change:   2022.01.28
-------------------------------------------------------------------------------
"""
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from Ch15.s15_03.ui_dialog import Ui_CDialog


class CDialog(QDialog, Ui_CDialog):
    def __init__(self, parent=None):
        super(CDialog, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = CDialog()
    widget.show()
    sys.exit(app.exec_())
